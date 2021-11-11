import pymongo
from flask import request
class mongo:

    def __init__(self):
        mongodb_client = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
        self.db = mongodb_client["Website"]
    
    #function returns all users from db
    def get_users(self,my_col):

        """This method returns all the users from the db
            and returns a list of all users
        Args:
        -----
            my_col (str):  The name of the users collection
        Returns:
        --------
            x[dict]:  User from db
        """

        mycol = self.db[my_col]
        users = mycol.find()
        for user in users:
            yield user

    #function returns specific user from db
    def get_user(self,my_col, id):

        """This method returns a specific user from the db
        Args:
        -----
            my_col (str):  The name of the users collection
            id (str): The user's id 
        Returns:
        --------
            list[dict]: User from db
        """
        mycol = self.db[my_col]
        user = mycol.find_one({"id": id})
        return user


    #function checks if user exists
    def check_if_user(self, my_col, email):

        """This method checks if user exists in db
        Args:
        -----
            my_col (str):  The name of the users collection
            email (str): The user's email
        Returns:
        --------
            boolean (True/False): True if user is in the db, else, False
        """
        mycol = self.db[my_col]

        email_found = mycol.find_one({"e-mail": email})
        if email_found != None:
            return True
        return False


    #function adds user
    def add_user(self,my_col, user_input):

        """This method adds user to db
        Args:
        -----
            my_col (str):  The name of the users collection
            user_input(dict): {"first_name": "", "last_name": "", "id": "", "e-mail": "", "Book_name": "", "password": ""}
        Returns:
        --------
            message (str): update about the status of the function
        """

        mycol = self.db[my_col]
        message = ''
            
        #checking if user exists
        if self.check_if_user(user_input["e-mail"], mycol):
            message = 'This email already exists in database'
            
        #adding user
        else:
            mycol.insert_one(user_input)
            message = 'Logged successfully'
        return message


    #Login function
    def login(self, my_col, user_input):

        """This method gets email and password and checks if user
           exists in db, else, returns message that user is not found
        Args:
        -----
            my_col (str):  The name of the users collection
            user_input(dict): {"e-mail": "", "password": ""}
        Returns:
        --------
            message (str): update about the status of the function
        """
        mycol = self.db[my_col]
        message = ''
            
        #checking if user exists
        if self.check_if_user(user_input["e-mail"], mycol):
            if user_input["password"] == mycol.find_one({"e-mail": user_input["e-mail"]})["password"]:
                message = 'Logged successfully'
            else:
                message = 'Password is incorrect'
        
        #user isn't in db
        else:
            message = 'User Not Found'
        return message


    #function updates user's book
    def update_book(self, my_col, user_input):

        """This method gets id and Book from the user
           and updates the book name 
        Args:
        -----
            my_col (str):  The name of the users collection
            user_input(dict): {"id": "", "Book_name": ""}
        Returns:
        --------
            message (str): update about the status of the function
        """
        mycol = self.db[my_col]
        
        #update book by user id
        user = mycol.find_one_and_update( {"id" : user_input["id"]}, {"$set": {"Book_name": user_input["Book_name"]} },upsert=True)
        
        message = 'Book updated'
        return message


    #function deletes user by id
    def delete_user(self, my_col, user_input):

        """This method gets user's email and deletes
           user from db
        Args:
        -----
            my_col (str):  The name of the users collection
            user_input(dict): {"email": ""}
        Returns:
        --------
            message (str): update about the status of the function
        """
        mycol = self.db[my_col]
        message = ''

        #checking if user exists
        if self.check_if_user(user_input["e-mail"], mycol):
            #delete user
            mycol.delete_one( {"e-mail" : user_input["e-mail"]} )
            message = 'User Deleted'

        #delete user by id
        else:
            message = 'User Not Found'
        return message


    #adding message to db
    def add_message(self, my_col, chat_data):
        """    
           This method gets chats data, finds the specific chat by the room id
           and adds message to the chat's list

           Args:
           -----
               my_col (str):  The name of the chat collection
               user_input(dict): {"room_id":id(str), "chat: ['msg': (str), 'date': (str), 'who_sent': id(str)]"}
           Returns:
           --------
               message (str): update about the status of the function
        """

        mycol = self.db[my_col]

        #add new message to chat list
        instance_found = find_room(my_col, chat_data["room_id"])
        updated_chat = instance_found["chat"].append(chat_data["chat"])

        #add to db
        instance_found = mycol.find_one_and_update( {"room_id" : chat_data["room_id"]}, {"$set": {"chat": updated_chat} },upsert=True)

        message = 'Book updated'
        return message


    #returns room by id
    def find_room(self, my_col, room_id):
        """    
           This method gets room id and returns the room instance 
           from the db

           Args:
           -----
               my_col (str):  The name of the chat collection
               room_id (str): The room id of the wanted room
           Returns:
           --------
               room (dict): instance from the Chat's collection
        """
        mycol = self.db[my_col]
        room = mycol.find_one({"room_id": room_id})
        return room



    #creating room
    def create_room(self, my_col, room_id):
        """    
           This method gets room id, creates room instance
           and returns message

           Args:
           -----
               my_col (str):  The name of the chat collection
               room_id (str): The room id of the wanted room
           Returns:
           --------
               message (str): update about the status of the function
        """
        mycol = self.db[my_col]

        #creating chat instance
        json = {"room_id": room_id, "chat": []}
        mycol.insert_one(json)
        
        message = 'New Chat Created'
        return message


    #function checks if room exists
    def check_room_exists(self, my_col, room_id):
        """    
           This method gets room id, checks if room instance
           exists in the Chat collection

           Args:
           -----
               my_col (str):  The name of the chat collection
               room_id (str): The room id of the wanted room
           Returns:
           --------
               message (str): update about the status of the function
        """
        mycol = self.db[my_col]
        if find_room(my_col, room_id) != None:
            return True
        return False


    #function returns specific chat from db
    def get_chat(self,my_col, room_id):
        """    
           This method gets room id, gets the chat from
           the instance in the Chat collection and return the chat list

           Args:
           -----
               my_col (str):  The name of the chat collection
               room_id (str): The room id of the wanted room
           Returns:
           --------
               chat (list): The chat list from the specific room
        """
        mycol = self.db[my_col]
        chat_col = find_room(my_col, room_id)
        chat = chat_col["chat"]
        return chat

    




    







