from flask import Flask, request, jsonify, render_template
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)  # Permite solicitudes desde dominios diferentes

# Configuración de la base de datos
db_config = {
    'host': 'dbimannov3.ch00woi2qdij.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'imanno007!',
    'database': 'eif037975979DB',
    'port': 3306  # Puerto predeterminado de MySQL
}

# Ruta principal para servir la página HTML
@app.route('/')
def home():
    return render_template('index.html')  # Sirve el archivo index.html

# Ruta para insertar datos en la base de datos
@app.route('/insertar', methods=['POST'])
def insertar():
    data = request.json
    nombre = data['nombre']
    edad = data['edad']
    telefono = data['telefono']
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, edad, telefono) VALUES (%s, %s, %s)", (nombre, edad, telefono))
        conn.commit()
        print(f"Datos recibidos: {data}")
        return jsonify({'message': 'Datos insertados correctamente'}), 200
    except mysql.connector.Error as err:
        print(f"Error en la base de datos: {err}")  # Esto mostrará el error en la terminal
        return jsonify({'error': f"Error en la base de datos: {err}"}), 500
    finally:
        cursor.close()
        conn.close()


# Ruta para obtener los datos de los usuarios registrados
@app.route('/obtener', methods=['GET'])
def obtener():
    try:
        # Conecta a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Ejecuta la consulta para obtener todos los usuarios
        cursor.execute("SELECT * FROM usuarios")
        datos = cursor.fetchall()

        return jsonify(datos), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Inicia el servidor en el puerto 5000
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
