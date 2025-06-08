from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory database
users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    # Return a list of all usernames
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    # Simple status check
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    # Return user data if user exists
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    # Parse JSON request data
    data = request.get_json()
    username = data.get('username')

    if not username:
        # Return error if username is missing
        return jsonify({"error": "Username is required"}), 400

    # Add the new user to the in-memory dictionary
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    # Return confirmation message with user data
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    # Run the development server
    app.run()
