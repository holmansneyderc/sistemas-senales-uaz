

from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import numpy as np
import os

app = Flask(__name__, static_folder='build')


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
    
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path != "" and os.path.exists("build/" + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
