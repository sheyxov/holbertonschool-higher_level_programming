#!/usr/bin/python3
"""Flask API implementing Basic Auth, JWT Auth, and Role-based Access."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Basic Auth handler
auth = HTTPBasicAuth()

# In-memory users
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# -------------------------
# BASIC AUTHENTICATION
# -------------------------
@auth.verify_password
def verify_password(username, password):
    """Verify Basic Auth credentials."""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Basic auth protected endpoint."""
    return "Basic Auth: Access Granted"


# -------------------------
# JWT AUTHENTICATION
# -------------------------
@app.route("/login", methods=["POST"])
def login():
    """Login and generate JWT token."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Add username + role to JWT token payload
    additional_claims = {"role": users[username]["role"]}
    token = create_access_token(identity=username, additional_claims=additional_claims)

    return jsonify({"access_token": token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """JWT-protected endpoint."""
    return "JWT Auth: Access Granted"


# -------------------------
# ROLE-BASED ACCESS
# -------------------------
@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Only admins allowed."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# -------------------------
# JWT ERROR HANDLERS (REQUIRED BY CHECKER)
# -------------------------
@jwt.unauthorized_loader
def unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    app.run()
#!/usr/bin/python3
"""Flask API implementing Basic Auth, JWT Auth, and Role-based Access."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Basic Auth handler
auth = HTTPBasicAuth()

# In-memory users
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# -------------------------
# BASIC AUTHENTICATION
# -------------------------
@auth.verify_password
def verify_password(username, password):
    """Verify Basic Auth credentials."""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Basic auth protected endpoint."""
    return "Basic Auth: Access Granted"


# -------------------------
# JWT AUTHENTICATION
# -------------------------
@app.route("/login", methods=["POST"])
def login():
    """Login and generate JWT token."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Add username + role to JWT token payload
    additional_claims = {"role": users[username]["role"]}
    token = create_access_token(identity=username, additional_claims=additional_claims)

    return jsonify({"access_token": token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """JWT-protected endpoint."""
    return "JWT Auth: Access Granted"


# -------------------------
# ROLE-BASED ACCESS
# -------------------------
@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Only admins allowed."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# -------------------------
# JWT ERROR HANDLERS (REQUIRED BY CHECKER)
# -------------------------
@jwt.unauthorized_loader
def unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    app.run()
