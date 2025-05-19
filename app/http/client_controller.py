import requests
import os
import time
from dotenv import load_dotenv
from app.repositories.clientes import ClientesRepository

def enviar_clientes(clientes):
    clienteRepository = ClientesRepository()
    
    load_dotenv()

    token = os.getenv('API_KEY')
    url_api = os.getenv('URL_RENAVE')
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
        }
    
    if not token:
        print("Erro: A variável de ambiente `API_TOKEN` não está definida.")
        exit()

    for cliente in clientes:
        try:
            # celular = int(cliente["CELULAR"]) if cliente["CELULAR"] else None
            id_cliente = cliente['CNPJ'] if cliente['CPF'] in [None, ''] else cliente['CPF']
            endereco = cliente['ENDERECO'].split(",")[0]
            numero = cliente['ENDERECO'].split(",")[1].strip() # strip remove os espaços extras

            clientes_data = {
                "id": id_cliente,
                "tipoPessoa": cliente['PESSOA'],
                "razaoSocial": cliente['RAZAO_SOCIAL'],
                "cep": str(cliente['CEP'] if cliente['CEP'] is not None else ""),
                "logradouro": endereco,
                "numero": str(numero), 
                "bairro":cliente['BAIRRO'],
                "cidade":cliente['NOME_CIDADE'],
                "uf": cliente['UF'],
            }

            url = f"{url_api}/{cliente['CNPJ_EMPRESA']}/client"

            response = requests.post(url, json=clientes_data, headers=headers)

            if (response.status_code == 409):
                print(response.status_code, response.json())
                clienteRepository.update_clientes(cliente['CODIGO'])
            elif (response.status_code == 403):
                print(response.status_code, response.json())
                break
            elif (response.status_code == 400):
                print(response.status_code, response.json())
            elif response.status_code == 401:
                print(response.status_code, response.json())
                break
            elif response.status_code == 500:
                print(response.status_code, response.json())
            elif response.status_code == 201:
                clienteRepository.update_clientes(cliente['CODIGO'])
                print(response.json())

        except Exception as e:
            print(e)
        
        time.sleep(5)

def atualizar_clientes():
    pass