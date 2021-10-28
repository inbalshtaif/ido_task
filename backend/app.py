from flask import Flask, render_template, jsonify, request
import json
import flask
from mongo import mongo

app=Flask(__name__,template_folder='template')
mongo = mongo()

@app.route("/")
def index():
    user = {'username': 'Inbal'}
    return render_template('index.html', title='Home', user=user)




@app.route("/get_Users", methods=['GET'])
def get_Users():
    return str(list(mongo.get_users("Users")))


@app.route("/get_User/<string:id>", methods=['GET'])
def get_User(id):
    return str(mongo.get_user("Users", id))




'''@app.route("/add_user")
def add_one(): 
    db.Users.insert_one({"first_name": "Shosha", "last_name": "Abutbul", "id": "10", "e-mail": "shosha@abut.com", "Book_name": "Fuck Reading"})
    return flask.jsonify(message="success")'''


if __name__ =="__main__":
    app.run(debug=True,port=8080)