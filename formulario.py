import psycopg2

IP_DB = "localhost"
PORT_DB ="5432"
DBNAME_BDB ="PROYECTO"
USER_DB ="postgres"
PASSWORD_DB = "root"

# Connect to your PostgreSQL database on a remote server
conn = psycopg2.connect(host=IP_DB, port=PORT_DB, dbname=DBNAME_BDB, user=USER_DB, password=PASSWORD_DB)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a test query
cur.execute("SELECT * FROM USUARIOS")

# Retrieve query results
records = cur.fetchall()

# Finally, you may print the output to the console or use it anyway you like
print(records)