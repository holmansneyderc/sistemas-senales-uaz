from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)  # Esto habilita CORS para toda la aplicación

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

if __name__ == '__main__':
    app.run(debug=True)
