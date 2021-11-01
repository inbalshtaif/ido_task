from flask import Flask, render_template, jsonify, request
import json
import flask
from mongo import mongo

app=Flask(__name__,template_folder='template')
mongo = mongo()

#main page
@app.route("/")
def index():
    user = {'username': 'Inbal'}
    return render_template('index.html', title='Home', user=user)


#Registration 
@app.route("/add_User", methods=['Post', 'Get'])
def register():

    if request.method == "POST": 
        content = request.get_json()

    message = mongo.add_user("Users", content)
    return message


#Login
@app.route("/login", methods=['Post', 'Get'])
def login():

    if request.method == "POST": 
        content = request.get_json()

    message = mongo.login("Users", content)
    return message


#update Book
@app.route("/update_book", methods=['Post', 'Get'])
def update_book():
    content = request.get_json()
    return mongo.update_book("Users", content)


#delete user
@app.route("/delete_user", methods=['Delete'])
def delete_user():
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


if __name__ =="__main__":
    app.run(debug=True,port=8080)