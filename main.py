import schedule
import json
import time

from app.http.client_controller import enviar_clientes
from app.repositories.clientes import ClientesRepository

from app.http.vehicle_controller import enviar_veiculos
from app.repositories.vehicles import VeiculosRepository

def agendador_enviar_clientes():
    print('Executando Busca de clientes...')
    clientes = ClientesRepository()
    data = json.loads(clientes.get_clientes())
    enviar_clientes(data)

def agendador_enviar_veiculos():
    print('Executando Busca de veiculos...')
    veiculos = VeiculosRepository()
    data = json.loads(veiculos.get_veiculos())
    enviar_veiculos(data)

schedule.every(30).minutes.do(agendador_enviar_clientes)
schedule.every(30).minutes.do(agendador_enviar_veiculos)

print('Aplicação rodando...')

# veiculos = VeiculosRepository()

# data = json.loads(veiculos.get_veiculos())
# enviar_veiculos(data)

clientes = ClientesRepository()

# data = json.loads(clientes.get_clientes())
# enviar_clientes(data)

while True:
    schedule.run_pending()

    time.sleep(3)