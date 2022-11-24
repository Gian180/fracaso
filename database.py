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


    def delete_data(self,nombre_tabla, id_user):
        self.cur = self.conn.cursor()
        self.consulta = f"DELETE FROM {nombre_tabla} WHERE iden = {id_user}"
        
        self.a = self.cur.execute(self.consulta)
        print(f"DELETE from {nombre_tabla} WHERE IDEN = 5")
        print(self.a)