import json
from app.repositories.firebird import FirebirdService

class VeiculosRepository(FirebirdService):
    def __init__(self):
        super().__init__() # Chama a classe pai

    def get_veiculos(self):
        try:
            conn = self.connect()

            cur = conn.cursor()
            cur.execute('select CNPJ_EMPRESA, ' \
            'CODIGO, NOVO_VELHO, DESCRICAO, CHASSI, ANO_FAB, ANO_MODELO, PLACA, RENAVAM, STATUS ' \
            'from DB_VEICULOS WHERE STATUS = 0')

            colunas = [desc[0].strip() for desc in cur.description]

            veiculos = [dict(zip(colunas, linha)) for linha in cur.fetchall()]

            self.close()

            return json.dumps(veiculos, indent=4, ensure_ascii=False)
        
        except Exception as e:
            print(e)
            return None

    def update_veiculos(self, codigo):
        try:
            conn = self.connect()
            cur = conn.cursor()
            cur.execute(f'update db_veiculos set status = 1 where codigo = {codigo}')

            conn.commit()
            self.close()

            print(f'Veiculo {codigo} enviado')
        except Exception as e:
            print(e)

