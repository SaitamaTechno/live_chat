from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message sent")
def handle_message(data):
    emit("new message", {"username": data["username"], "message": data["message"]}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0")
