# Today we are gonna build API = Application Program Interface with Flask(micro web framework for web development and creating API's) from the scratch.

'''
Theory: 
 - API is a set of rules and protocols that allows one software application to communicate with each other.
 - It can handle different request.
 
 - An API is just an interface of callable functions. It can be a code library that simplifies some complex tasks,
   a web API (which is what this video talks about) or a bunch of functions that a running process on your computer 
   exposes for other programs to interact with
'''

# Flask wil be the server that we are running API on.

# we can use pip install Flask to install flask at first and then import dependencies.

from flask import Flask, jsonify, request

# Flask app named app
app = Flask(__name__)

# Creating root: it's like a end point in API(like location on API)

@app.route("/")    # "/" default root
def root_home():
    return "Root Home"


@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Lhasang Lama",
        "email": "john.doe@example.com"
    }
    
    # query parameter: extra value after the mian path
    
    extra = request.args.get("extra")
    if extra:
        user_id["extra"] = extra
    # Below allows flask to parse this value and return JSON data
    return jsonify(user_data), 200    # JSON: JavaScript Object Notation

# (HTTP = communicating data over internet)
# We know that whenever we are working with API we are working with the HTTP methods(Hyper Text Transfer Protocal)


# lets crate a put root

@app.route("/create_user/", methods = ["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
    
