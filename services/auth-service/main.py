from flask import Flask, jsonify, request
import jwt
import datetime

app = Flask(__name__)
SECRET_KEY = "your-secret-key"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    token = jwt.encode({
        "user": data.get("username"),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, SECRET_KEY, algorithm="HS256")
    return jsonify(token=token)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
