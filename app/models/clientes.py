class Clientes: 
    @staticmethod
    def to_dict(clientes):
        clientes_dict = []

        for cliente in clientes:
            clientes_dict = cliente.copy()

            