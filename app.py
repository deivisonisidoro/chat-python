from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
io = SocketIO(app)


messages = []


@app.route("/")
def home():
  return render_template("chat.html")

@io.on('sendMessage')
def send_message_handler(msg):
  messages.append(msg)
  emit('getMessage', msg, broadcast=True)

@io.on('message')
def message_handler(msg):
    send(messages)
if __name__ == '__main__':
    io.run(app, debug= True)
