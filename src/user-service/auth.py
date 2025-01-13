from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import logging
import bcrypt

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your-secret-key"  # Change this in production
jwt = JWTManager(app)

# Dummy user data with roles and hashed passwords
users = {
    "user1": {"password": bcrypt.hashpw("password123".encode('utf-8'), bcrypt.gensalt()), "role": "user"},
    "admin": {"password": bcrypt.hashpw("adminpass".encode('utf-8'), bcrypt.gensalt()), "role": "admin"}
}

@app.route("/login", methods=["POST"])
def login():
    try:
        username = request.json.get("username", None)
        password = request.json.get("password", None)

        if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username]["password"]):
            access_token = create_access_token(identity=username, additional_claims={"role": users[username]["role"]})
            refresh_token = create_refresh_token(identity=username)
            return jsonify(access_token=access_token, refresh_token=refresh_token), 200
        else:
            logger.warning(f"Failed login attempt for {username}")
            return jsonify(message="Invalid credentials"), 401
    except Exception as e:
        logger.error(f"Error during login: {str(e)}")
        return jsonify(message="An error occurred"), 500

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    try:
        claims = get_jwt_identity()
        if claims["role"] == "admin":
            return jsonify(message="Welcome, admin!")
        else:
            logger.warning(f"Unauthorized access attempt by {claims['identity']}")
            return jsonify(message="You are not authorized to access this page"), 403
    except Exception as e:
        logger.error(f"Error in protected route: {str(e)}")
        return jsonify(message="An error occurred"), 500

if __name__ == "__main__":
    app.run(debug=True)
