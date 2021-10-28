import pymongo
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
        

    