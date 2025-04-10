import json
from app.repositories.firebird import FirebirdService

class ClientesRepository(FirebirdService):
    def __init__(self):
        super().__init__() # Chama a classe pai

    def get_clientes(self):
        try:
            conn = self.connect()

            cur = conn.cursor()
            cur.execute('select CNPJ_EMPRESA, ' \
            'CNPJ, RAZAO_SOCIAL, CODIGO, CEP, ENDERECO, PESSOA,' \
            'BAIRRO, UF, CELULAR, CPF, TELEFONE, NOME_CIDADE, COMPLEMENTO from db_clientes WHERE STATUS = 0')

            colunas = [desc[0].strip() for desc in cur.description]

            clientes = [dict(zip(colunas, linha)) for linha in cur.fetchall()]

            self.close()

            return json.dumps(clientes, indent=4, ensure_ascii=False)
        
        except Exception as e:
            print(e)
            return None

    def update_clientes(self, codigo):
        try:
            conn = self.connect()
            cur = conn.cursor()
            cur.execute(f'update db_clientes set status = 1 where codigo = {codigo}')

            conn.commit()
            self.close()

            print(f'Cliente {codigo} enviado')
        except Exception as e:
            print(e)

