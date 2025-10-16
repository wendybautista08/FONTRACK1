from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pago')
def pago():
    return render_template('pago.html')

@app.route('/procesar_pago', methods=['POST'])
def procesar_pago():
    nombre = request.form['nombre']
    email = request.form['email']
    metodo = request.form['metodo']
    print(f"Pago recibido de {nombre}, Email: {email}, Método: {metodo}")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
