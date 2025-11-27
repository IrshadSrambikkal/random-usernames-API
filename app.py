from flask import Flask, jsonify, render_template
import random
import string

app = Flask(__name__)

def generate_username():
    words = ["cyber", "alpha", "nova", "pixel", "shadow", "code", "neo", "matrix"]
    word = random.choice(words)
    numbers = ''.join(random.choices(string.digits, k=4))
    return word + numbers

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["GET"])
def generate():
    username = generate_username()
    return jsonify({"username": username})

if __name__ == "__main__":
    app.run(debug=True)
