import psycopg2
from constantes import *

class DataBase:
    
    def __init__(self):
        self.conn = psycopg2.connect(host=IP_DB, port=PORT_DB, dbname=DBNAME_BDB, user=USER_DB, password=PASSWORD_DB)
        self.cur = self.conn.cursor()
        print("se hizo la coneccion")
        
    def get_data_DB(self,nombre_tabla):
        self.cur.execute(f"SELECT * FROM {nombre_tabla}")
        self.records = self.cur.fetchall()
        
        return self.records
