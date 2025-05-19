import requests
import os
import time
from dotenv import load_dotenv
from app.repositories.vehicles import VeiculosRepository

def enviar_veiculos(veiculos):
    load_dotenv()
    veiculosRepository = VeiculosRepository()

    token = os.getenv('API_KEY')
    url_api = os.getenv('URL_RENAVE')
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    if not token:
        print("Erro: A variável de ambiente `API_TOKEN` não está definida.")
        exit()

    for veiculo in veiculos:
        try:
            veiculos_data = {
                "tipoVeiculo": veiculo['NOVO_VELHO'],
                "chassi": veiculo['CHASSI'],
                "descricao":veiculo['DESCRICAO'],  # Falta no banco
                "anoFabricacao": veiculo['ANO_FAB'],
                "anoModelo":veiculo['ANO_MODELO'],
                "placa":veiculo['PLACA'],
                "renavam": veiculo['RENAVAM'],
            }

            url = f"{url_api}/{veiculo['CNPJ_EMPRESA']}/vehicle"

            response = requests.post(url, json=veiculos_data, headers=headers)

            if response.status_code == 201:
                print('Veículo cadastrado com sucesso')
                veiculosRepository.update_veiculos(veiculo['CODIGO'])
            else :
                print(response.text)
        except Exception as e:
            print(e)

        time.sleep(5)

    def atualizar_carros():
        pass