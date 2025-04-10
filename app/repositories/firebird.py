from firebird.driver import connect

class FirebirdService:
    def __init__(self):
        self.database = 'speedautomac.ddns.net:/database/Servicos/denatran.fdb'
        self.user = 'sysdba'
        self.password = 'masterkey'
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = connect(
                database=self.database,
                user=self.user,
                password=self.password
            )
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None