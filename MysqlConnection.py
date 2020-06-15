import Empresa
import mysql.connector
from mysql.connector.fabric.connection import MySQLFabricConnection


class MysqlConnection:
    __instance__ = None
    _connection: mysql.connector = None
    _cursor:MySQLFabricConnection

    def __init__(self):
        """ Constructor.
       """
        if MysqlConnection.__instance__ is None:
            MysqlConnection.__instance__ = self
        else:
            raise Exception("You cannot create another MysqlConnection class")

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
       """
        if not MysqlConnection.__instance__:
            MysqlConnection()
        return MysqlConnection.__instance__

    def set_connection(self, host: str, user: str, passwd: str, database:str):
        # host = the database server ip address
        # user = the database user
        # passwd = the database user password
        self._connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )
        self.__set_cursor()

    # 'private' method
    def __set_cursor(self):
        self._cursor = self._connection.cursor()

    def get_empresas(self):
        pass
