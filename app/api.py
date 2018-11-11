from flask import Flask
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
 
import requests
import card_methods

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print('Connection successful')

@socketio.on('message_sent')
def display_message(message):
    data = ceea_ce_primesc_de_la_chatbotu_pizdii(message) #de apelat functia de la baieti
    emit("response_sent", data)

@socketio.on("my_event")
def show_event(data):
    print("Response from Goje is: ", data)

#mai jos ma astpt sa primesc un json sa vad daca este personalizat sau nu, si cu brand si value
@socketio.on("card_selected")
def fetch_card_code(json):
    if json["personalised"] == True:
        return true

    else:
        return card_methods.issue_digital_card(brand=json['brand'], value=json['value'])





if __name__ == '__main__':
    socketio.run(app)