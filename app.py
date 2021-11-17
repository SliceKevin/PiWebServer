from flask import Flask, render_template
import mariadb

conn=mariadb.connect(
	host='127.0.0.1',
	port= 3306,
	user='root',
	password='WaffleIron',
	database='information_schema')

app = Flask(__name__)

cur = conn.cursor()
results = cur.execute('SELECT * FROM Keywords')
rows = cur.fetchall()


conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

@app.route('/data')
def data():
    return render_template('display.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
