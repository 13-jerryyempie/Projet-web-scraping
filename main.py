from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    # Changer host de 127.0.0.1 à 0.0.0.0 pour permettre l'accès externe
    app.run(host="0.0.0.0", port=5000, debug=True)
