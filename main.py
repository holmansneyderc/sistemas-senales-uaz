from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from sympy import symbols, lambdify
import numpy as np
import os

app = Flask(__name__, static_folder='build')
CORS(app) 

def convertir_expresion(expresion_condicional):
    # Reemplaza '&&' por 'and'
    expresion_condicional = expresion_condicional.replace('&&', 'and')
    # Reemplaza '?' por 'if' y ':' por 'else'
    expresion_condicional = expresion_condicional.replace('?', 'if').replace(':', 'else')
    return expresion_condicional


@app.route('/convolve', methods=['POST'])
def convolve():
    try:
        data = request.get_json()
        impulse_data_left = np.array(data['impulseDataLeft'])
        impulse_data_right = np.array(data['impulseDataRight'])

        # Realizamos la convolución
        result = np.convolve(impulse_data_left, impulse_data_right, mode='full')
        return jsonify(result.tolist())

    except Exception as e:
        return jsonify(error=str(e)), 400
    
@app.route('/convolve-continue', methods=['POST'])
def convolvecontinue():
    try:
        data = request.get_json()
        expression_left = data['impulseDataLeft']
        expression_right = data['impulseDataRight']

        # Definir el símbolo x
        x = symbols('x')

        # Crear funciones a partir de las expresiones
        func_left = lambdify(x, convertir_expresion(expression_left), 'numpy')
        func_right = lambdify(x, convertir_expresion(expression_right), 'numpy')

        # Definir el rango de x para la convolución
        x_range = list(range(-10, 11))  # Cambia esto según tus necesidades

        # Evaluar las funciones para obtener los valores de y
        y_left = [func_left(x_val) for x_val in x_range]
        y_right = [func_right(x_val) for x_val in x_range]

        # Realizar la convolución
        convolution_result = [y_left[i] * y_right[i] for i in range(len(x_range))]

        return jsonify({
            "convolution_result": convolution_result,
            "x_values": x_range
        })

    except Exception as e:
        return jsonify(error=str(e)), 400
    
   
@app.route('/animate-convolve-continue', methods=['POST'])
def convolvecontinueanimate():
    try:
        data = request.get_json()
        expression_left = data['impulseDataLeft']
        expression_right = data['impulseDataRight']

        # Definir el símbolo x
        x = symbols('x')

        # Crear funciones a partir de las expresiones
        func_left = lambdify(x, convertir_expresion(expression_left), 'numpy')
        func_right = lambdify(x, convertir_expresion(expression_right), 'numpy')

        # Definir el rango de x para la convolución
        x_range = list(range(-10, 11))  # Cambia esto según tus necesidades

        # Obtener el tiempo total de animación desde los datos del cliente
        animation_time = data.get('animationTime', 10.0)  # Valor predeterminado si no se proporciona
        num_frames = int(animation_time * 10)  # 10 frames por segundo

        # Inicializar una lista para almacenar las señales en función del tiempo
        signals_over_time = []

        # Realizar la animación en función del tiempo
        for frame in range(num_frames):
            t = frame / 10.0  # Incremento de tiempo por frame
            y_left = [func_left(x_val) for x_val in x_range]
            y_right = [func_right(x_val - t) for x_val in x_range]  # Desplaza la señal derecha en el tiempo
            convolution_result = [y_left[i] * y_right[i] for i in range(len(x_range))]
            signals_over_time.append({
                "signalLeft": y_left,
                "signalRight": y_right,
                "convolutionResult": convolution_result,
                "time": t
            })

        return jsonify({"signalsOverTime": signals_over_time, "x_values": x_range})

    
    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path != "" and os.path.exists("build/" + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
