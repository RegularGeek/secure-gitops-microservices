from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/products")
def products():
    return jsonify([{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Phone"}])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
