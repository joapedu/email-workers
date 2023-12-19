import redis
import json
import os
from time import sleep
from random import randint
from redis import ConnectionPool

def send_email(mensagem):
    try:
        # Simulando envio de e-mail...
        print('Mandando a mensagem:', mensagem['assunto'])
        sleep(randint(15, 30))
        print('Mensagem', mensagem['assunto'], 'enviada')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')

if __name__ == '__main__':
    try:
        redis_host = os.getenv('REDIS_HOST', 'queue')
        redis_pool = ConnectionPool(host=redis_host, port=6379, db=0)
        r = redis.StrictRedis(connection_pool=redis_pool)
        print('Aguardando mensagens ...')
        while True:
            _, mensagem = r.blpop('sender')
            mensagem = json.loads(mensagem)
            send_email(mensagem)
    except Exception as e:
        print(f'Erro ao aguardar mensagens: {e}')
