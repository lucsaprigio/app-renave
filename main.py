import schedule
import json
import time
from app.http.client_controller import enviar_clientes
from app.repositories.clientes import ClientesRepository

def agendador_enviar_clientes():
    print('Executando Busca de clientes...')
    clientes = ClientesRepository()
    data = json.loads(clientes.get_clientes())
    enviar_clientes(data)

schedule.every(1).minutes.do(agendador_enviar_clientes)

print('Aplicação rodando...')

while True:
    schedule.run_pending()
    time.sleep(1)