import psycopg2
import redis
import json
import os
import logging
from bottle import Bottle, request

class Sender(Bottle):
    def __init__(self):
        super().__init__()
        self.route('/', method='POST', callback=self.send)
        
        try:
            redis_host = os.getenv('REDIS_HOST', 'queue')
            self.fila = redis.StrictRedis(host=redis_host, port=6379, db=0)
            
            db_host = os.getenv('DB_HOST', 'db')
            db_user = os.getenv('DB_USER', 'postgres')
            db_name = os.getenv('DB_NAME', 'sender')
            dsn = f'dbname={db_name} user={db_user} host={db_host}'
            self.conn = psycopg2.connect(dsn)

        except Exception as e:
            logging.error(f'Erro ao inicializar banco de dados: {e}')
            raise

    def register_message(self, assunto, mensagem):
        try:
            with self.conn.cursor() as cur:
                SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'
                cur.execute(SQL, (assunto, mensagem))
                self.conn.commit()

                msg = {'assunto': assunto, 'mensagem': mensagem}
                self.fila.rpush('sender', json.dumps(msg))

                logging.info('Mensagem registrada!')
        
        except Exception as e:
            logging.error(f'Erro ao inserir mensagem no sistema: {e}')
            raise

    def send(self):
        try:
            assunto = request.forms.get('assunto')
            mensagem = request.forms.get('mensagem')

            self.register_message(assunto, mensagem)

            return 'Mensagem enfileirada! Assunto: {} Mensagem: {}'.format(
                assunto, mensagem
            )
        
        except Exception as e:
            logging.error(f'Erro ao processar a solicitação: {e}')
            return 'Erro ao processar a solicitação.'

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    sender = Sender()
    sender.run(host='0.0.0.0', port=8080, debug=True)
