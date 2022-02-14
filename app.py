from flask import Flask, jsonify, request
import random

app = Flask("Guess The Number API")

number = 0

@app.route("/api/start_game")
def start_game():
    global number
    number = random.randint(1, 100)
    return "Game Started!"


@app.route("/api/guess_the_number", methods=["GET"])
def guess_the_number():
    guess = int(request.args.get("guess"))
    result = {"win": False, "state": ""}

    if guess < number:
        result["state"] = "lower"
    elif guess > number:
        result["state"] = "higher"
    else:
        result["win"] = True
        result["state"] = "equals"

    return jsonify(result)

debug = True
app.run(host="0.0.0.0", port=1337, debug=debug)