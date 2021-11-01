import pymongo
from flask import request
class mongo:

    def __init__(self):
        mongodb_client = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
        self.db = mongodb_client["Website"]
    
    #function returns all users from db
    def get_users(self,my_col):
        mycol = self.db[my_col]
        user = mycol.find()
        for x in user:
            yield x

    #function returns specific user from db
    def get_user(self,my_col, id):
        mycol = self.db[my_col]
        user = mycol.find_one({"id": id})
        return user


    #function checks if user exists
    def check_if_user(self, email, mycol):
        email_found = mycol.find_one({"e-mail": email})
        return email_found


    #function adds user
    def add_user(self,my_col, user_input):
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
        mycol = self.db[my_col]
        message = ''
        
        #update book by user id
        user = mycol.find_one_and_update( {"id" : user_input["id"]}, {"$set": {"Book_name": user_input["Book_name"]} },upsert=True)
        message = 'Book updated'
        
        return message


    #function deletes user by id
    def delete_user(self, my_col, user_input):
        mycol = self.db[my_col]
        message = ''

        #checking if user exists
        if self.check_if_user(user_input["e-mail"], mycol):
            mycol.delete_one( {"e-mail" : user_input["e-mail"]} )
            message = 'User Deleted'

        #delete user by id
        else:
            message = 'User Not Found'
        return message
        

    