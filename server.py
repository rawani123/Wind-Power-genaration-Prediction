from flask import Flask, jsonify, request


app = Flask(__name__)

# Endpoint to handle POST requests
@app.route('/post_example', methods=['POST'])
def post_example():
    data = request.json 
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
