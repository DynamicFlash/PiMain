from flask import Flask 
from flask_socketio import SocketIO, send,emit
import json
from regUsers import regNew
import atexit
from deluser import delU

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('connect')
def message():
	print('client connected')
	emit('piOnlineStatus', 'true')

@socketio.on('piReg')
def message(data):
	print('received message '+ data)
	user = json.loads(data)
	regNew(user)
	socketio.emit('piNewUser',data)

@socketio.on('disconnect')
def disconnect():
	print('disconnect ')
	socketio.emit('piOfflineStatus', 'true')

@socketio.on('piRegDel')
def delete(data):
	print('received data', data)
	user = json.loads(data)
	delU(user['name'])
	socketio.emit('piDelete',data)

if __name__ == '__main__':
	socketio.run(app)
