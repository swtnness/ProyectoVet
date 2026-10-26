import pymysql
from pymysql.cursors import DictCursor
from config.settings import DB_CONFIG

class Conexion:
    def conectar(self):
        return pymysql.connect(
            cursorclass=DictCursor,
            **DB_CONFIG
        )
