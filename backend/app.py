from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO
import json
import flask
from mongo import mongo

app = Flask(__name__,template_folder='template')
socketio = SocketIO(app)
mongo = mongo()

#main page
@app.route("/")
def index():
    return render_template('index.html', title='Home')


#Registration 
@app.route("/add_User", methods=['Post', 'Get'])
def register():
    """expects - {"first_name": "", "last_name": "", "id": "", "e-mail": "", "Book_name": "", "password": ""}"""

    if request.method == "POST": 
        content = request.get_json()

    message = mongo.add_user("Users", content)
    return message


#Login
@app.route("/login", methods=['Post', 'Get'])
def login():
    """expects - {"e-mail": "", "password": ""}"""

    if request.method == "POST": 
        content = request.get_json()

    message = mongo.login("Users", content)
    return message


#update Book
@app.route("/update_book", methods=['Post', 'Get'])
def update_book():
    """expects - {"id": "", "Book_name": ""}"""

    content = request.get_json()
    return mongo.update_book("Users", content)


#delete user
@app.route("/delete_user", methods=['Delete'])
def delete_user():
    """expects - {"email": ""}"""

    content = request.get_json()
    return mongo.delete_user("Users", content)


#getting all users
@app.route("/get_Users", methods=['GET'])
def get_Users():
    return str(list(mongo.get_users("Users")))


#getting specific user by id
@app.route("/get_User/<string:id>", methods=['GET'])
def get_User(id):
    return str(mongo.get_user("Users", id))


#joining new room
@socketio.on('join')
def join_new_room(self, room_id, methods=['GET', 'POST']):
    data = json.loads(room_id)

    #check if the room exists
    if mongo.check_room_exists("Chat", data["room_id"]):
        join_room(data["room_id"])
    else:
        #creating new room
        print(mongo.create_room("Chat", data["room_id"]))
        join_room(data["room_id"])

    #sending assurance that client entered the room
    user = mongo.get_user("Users", data["user1_id"])
    send(user['fname'] + ' has entered the room.', to=data["room_id"])


#handling message
@socketio.on('handle_message')
def handle_message(self, chat_data, methods=['GET', 'POST']):
    """expects - {"room_id":id(str), "chat: ['msg': (str), 'date': (str), 'who_sent': id(str)]"}"""

    data = json.loads(chat_data)
    print(mongo.add_message("Chat", data))
    emit(data, to=data["room_id"])



#getting specific chat by id
@app.route("/get_Chat/<string:id>", methods=['GET'])
def get_chat(self, room_id):
    return str(mongo.get_chat("Chat", room_id))
    


if __name__ =="__main__":
    socketio.run(app, debug=True, port=8080)