# API for interacting with Penrose Institute modules

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/tiling', methods=['GET'])
def get_tiling():
    return jsonify({
        'status': 'success',
        'data': 'Penrose Tiling Data'
    })

if __name__ == '__main__':
    app.run(debug=True)
