from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def calculoNota():
    if request.method == 'POST':
        numero1 = int(request.form['numero1'])
        numero2 = int(request.form['numero2'])
        numero3 = int(request.form['numero3'])
        numero4 = int(request.form['numero4'])
        promedio = (numero1 + numero2 + numero3) / 3
        if numero4 >= 75 and promedio >= 40:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"
        return render_template('ejercicio1.html', numero1=numero1, numero2=numero2, numero3=numero3, numero4=numero4, promedio=promedio, estado=estado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def nombreMasLargo():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]

        nombre_mas_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)

        return render_template('ejercicio2.html', nombre_mas_largo=nombre_mas_largo, cantidad_caracteres=cantidad_caracteres)

    return render_template('ejercicio2.html')



if __name__ == '__main__':
    app.run(debug=True)
