from flask import Flask,request,jsonify

app=Flask(__name__)  #starts the flask app

user={} #In-memory storage

@app.route('/') #when you visit the root url '/'
def home():
    return "welcome to user api"  #return a simple msg to show the api is running.

@app.route('/users',methods=['GET']) #read operation.
def get_user():
    
    return jsonify(user) #converts the py dic 'users' into json and return.

@app.route('/users',methods=['POST'])  #create operation.
def add_user():
    data=request.get_json()  #get the json data sent inthe request body.
    user_id=len(user)+1 #generate the new user id
    user[user_id]=data   #store in the dic

    return jsonify({"id":user_id,"message":"User added"}),200

@app.route('/users/<int:user_id>',methods=['PUT'])  #update operation
def update_user(user_id):
    if user_id not in user:
        return jsonify({"error":"user not found"}),404
    
    data = request.get_json()
    user[user_id].update(data)

    return jsonify({"id": user_id, "updated_user": user[user_id], "message": "User updated"}), 200
    
    
    data=request.get_json()

    user[user_id].update(data)
    return jsonify({"message": "User updated", "user": user[user_id]})



@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
    if user_id not in user:
        return jsonify({"error":"user is not found"}),404
    del user[user_id]
    return jsonify({"message":"user deleted"})

if __name__=="__main__":
    app.run(debug=True)





