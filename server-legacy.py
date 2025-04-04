import psycopg2
import random
import string
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite requisições de qualquer origem

# Configuração do banco de dados PostgreSQL
DB_NAME = "mydatabase"
DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"  # Ou o IP do servidor PostgreSQL
DB_PORT = "5432"  # Padrão do PostgreSQL

# Conectar ao banco
def connect_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

# Criar tabela no PostgreSQL
def create_database():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dogs (
            ID SERIAL PRIMARY KEY,
            ownerFullName TEXT,
            ownerAdress TEXT,
            ownerMobileNumber TEXT,
            ownerMobileEmail TEXT,
            dogName TEXT,
            dogAge INTEGER,
            dogColor TEXT,
            dogSize TEXT,
            dogWeight REAL,
            dogTemper TEXT
        )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

# API para buscar um cachorro pelo ID
@app.route("/find_dog", methods=["GET"])
def find_dog():
    dog_id = request.args.get("id")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dogs WHERE ID = %s", (dog_id,))
    dog = cursor.fetchone()

    cursor.close()
    conn.close()

    if dog:
        return jsonify({
            "ID": dog[0],
            "ownerFullName": dog[1],
            "ownerAdress": dog[2],
            "ownerMobileNumber": dog[3],
            "ownerMobileEmail": dog[4],
            "dogName": dog[5],
            "dogAge": dog[6],
            "dogColor": dog[7],
            "dogSize": dog[8],
            "dogWeight": dog[9],
            "dogTemper": dog[10]
        })
    else:
        return jsonify({"error": "ID não encontrado"}), 404

if __name__ == "__main__":
    create_database()
    app.run(debug=True)
