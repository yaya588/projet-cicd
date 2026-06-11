from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def accueil():
    return jsonify({
        "message": "l3 info enastic"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)