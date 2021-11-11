# Mongodb
MongoDB is a nosql database stores data in documents like json.

Description: 
A library that combines all the functions interact with the database.
The database includes two collections: users, chat.

collections:
* Users {
    "_id": {"$oid": " "},
    "first_name": " ",
    "last_name": " ",
    "id": " ",
    "e-mail": " ",
    "Book_name": " ",
    "password": " "}
    }

* Chat {
    "_id":{"$oid":" "},
    "room_id":"",
    "chat":[{"msg":" ", "date":" ", "who_sent":" "}]
    }


functions:
* def get_users(self,my_col):
* def get_user(self,my_col, id):
* def check_if_user(self, my_col, email):
* def add_user(self,my_col, user_input):
* def login(self, my_col, user_input):
* def update_book(self, my_col, user_input):
* def delete_user(self, my_col, user_input):
* def add_message(self, my_col, chat_data):
* def find_room(self, my_col, room_id):
* def create_room(self, my_col, room_id):
* def check_room_exists(self, my_col, room_id):
* def get_chat(self,my_col, room_id):  



# app.py 

functions: 
* def index():
* def register():
* def login():
* def update_book():
* def delete_user():
* def get_Users():
* def get_User(id):
* def join_new_room(self, room_id, methods=['GET', 'POST']):
* def handle_message(self, chat_data, methods=['GET', 'POST']):
* def get_chat(self, room_id):

