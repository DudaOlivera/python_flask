from flask import Flask, render_template, request, redirect, url_for
import pymysql
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    """Estabelece uma conexão com o banco de dados"""
    connection = pymysql.connect(host=app.config['MYSQL_HOST'],
                                  user=app.config['MYSQL_USER'],
                                  password=app.config['MYSQL_PASSWORD'],
                                  database=app.config['MYSQL_DB'],
                                  port=app.config['MYSQL_PORT'])
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM produto")
    results = cursor.fetchall()

    connection.close()

    return render_template('index.html', results=results)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO produto (nome, preco) VALUES (%s, %s)", (nome, preco))
        connection.commit()

        connection.close()

        return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM produto WHERE id = %s", (id,))
    connection.commit()

    connection.close()

    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']

        cursor.execute("UPDATE produto SET nome = %s, preco = %s WHERE id = %s", (nome, preco, id))
        connection.commit()

        connection.close()

        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM produto WHERE id = %s", (id,))
    product = cursor.fetchone()

    connection.close()

    return render_template('update.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
