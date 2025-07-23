from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API Gateway"})

@app.route("/auth")
def auth_proxy():
    return requests.get("http://auth-service:5001/login").json()

@app.route("/products")
def products_proxy():
    return requests.get("http://product-service:5002/products").json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
