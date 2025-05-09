from firebird.driver import connect
from dotenv import load_dotenv
import os

load_dotenv()

database = os.getenv('DATABASE')
user = os.getenv('DATABASE_USER')
password = os.getenv('DATABASE_PASSWORD')

class FirebirdService:
    def __init__(self):
        self.database = database
        self.user = user
        self.password = password
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