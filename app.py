from flask import Flask, request, jsonify, render_template
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)  # Permite solicitudes desde dominios diferentes

# Configuración de la base de datos
db_config = {
    'host': 'eif037975979db.ch00woi2qdij.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'Pedro3103$A',
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
    data = request.json  # Obtiene los datos JSON enviados en el cuerpo de la solicitud
    nombre = data.get('nombre')
    edad = data.get('edad')
    telefono = data.get('telefono')

    if not nombre or not edad or not telefono:
        return jsonify({'error': 'Faltan campos'}), 400

    try:
        # Conecta a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Inserta los datos en la tabla Alumno
        cursor.execute("INSERT INTO Alumno (nombre, edad, telefono) VALUES (%s, %s, %s)", (nombre, edad, telefono))
        conn.commit()

        return jsonify({'message': 'Datos insertados correctamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
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
        cursor.execute("SELECT * FROM Alumno")
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
