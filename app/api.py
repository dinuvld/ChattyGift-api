from flask import Flask
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
 
import requests

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    print("Connected!")

@socketio.on('my_event', namespace='/test')
def display_message(message):
    print(message)


if __name__ == '__main__':
    socketio.run(app)