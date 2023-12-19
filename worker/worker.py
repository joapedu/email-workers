import redis
import json
import os
from time import sleep
from random import randint

def send_email(mensagem):
    try:
        # Simulando envio de e-mail...
        print('Mandando a mensagem:', mensagem['assunto'])
        sleep(randint(15, 30))
        print('Mensagem', mensagem['assunto'], 'enviada')
    except Exception as e:
        print(f'Erro ao enviar, verifique se a fila dos workers está cheia: {e}')

if __name__ == '__main__':
    try:
        redis_host = os.getenv('REDIS_HOST', 'queue')
        r = redis.Redis(host=redis_host, port=6379, db=0)
        print('Aguardando mensagens ...')
        while True:
            mensagem = json.loads(r.blpop('sender')[1])
            send_email(mensagem)
    except Exception as e:
        print(f'Não foi possível gerar as mensagens: {e}')
