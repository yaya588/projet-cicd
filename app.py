from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def accueil():
    return jsonify({
        "message": "version 2 du service"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)