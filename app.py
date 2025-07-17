from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Minhack004 Webhook!', 200

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return 'Webhook is ready.', 200
    elif request.method == 'POST':
        data = request.json
        print("Received:", data)
        return jsonify({'status': 'received', 'data': data}), 200
