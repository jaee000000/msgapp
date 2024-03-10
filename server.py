from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    send(message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)