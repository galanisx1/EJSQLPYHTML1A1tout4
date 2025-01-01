import mysql.connector

db_config = {
    'host': 'eif037975979db.ch00woi2qdij.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'Pedro3103$A',
    'database': 'eif037975979DB',
    'port': 3306
}

try:
    conn = mysql.connector.connect(**db_config)
    print("Conexión exitosa a la base de datos.")
    conn.close()
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
