from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python Docker Application!"

@app.route("/about")
def about():
    return "from about page Hello from Python Docker Application!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
