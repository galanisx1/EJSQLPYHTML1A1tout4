import mysql.connector

db_config = {
    'host': 'dbimannov3.ch00woi2qdij.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'imanno007!',
    'database': 'eif037975979DB',
    'port': 3306  # Puerto predeterminado de MySQL
}

try:
    conn = mysql.connector.connect(**db_config)
    print("Conexión exitosa a la base de datos.")
    conn.close()
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
