from socketio_client.manager import Manager
import json

import gevent
from gevent import monkey;
monkey.patch_socket()

io = Manager('http', 'localhost', 3000)
chat = io.socket('')

@chat.on_connect()
def on_connect():
	chat.emit('piOnlineStatus','true');

@chat.on('piReg')
def on_hello(*args):
	 with open('filePathNameWExt.json', 'w') as fp:
		json.dump(data, fp)

io.connect()
gevent.wait()