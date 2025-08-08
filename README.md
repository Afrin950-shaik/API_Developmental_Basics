#  Flask CRUD API

A simple **Flask** API that allows you to **Create**, **Read**, **Update**, and **Delete** user data using HTTP methods.

##  Features
- **POST** → Add a new user
- **GET** → Retrieve user details
- **PUT** → Update user information
- **DELETE** → Remove a user

## 🛠 Tech Stack
- **Python 3**
- **Flask**
- **Postman** (for API testing)

##  Project Structure
```
flask_crud/
│── app.py           # Main Flask app
```

##  How to Run
1️. Install dependencies
```bash
pip install flask
```
2️. Run the Flask server
```bash
python app.py
```
Server will start at:
```
http://127.0.0.1:5000
```

##  API Endpoints

###  Create User
**POST** `/users`
```json
{
    "Name": "John Doe",
    "Email": "john@example.com"
}
```

###  Get All Users
**GET** `/users`

###  Update User
**PUT** `/users/<user_id>`
```json
{
    "Name": "Updated Name",
    "Email": "updated@example.com"
}
```

###  Delete User
**DELETE** `/users/<user_id>`



## 🧑‍💻 Author
Shaik Afrin
