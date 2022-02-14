# How To Use (example)
import requests

start_game_req = requests.get("http://localhost:1337/api/start_game") # to start a new game you need to create a get request to http://localhost:1337/api/start_game

if start_game_req.status_code == 200:
    while True:
        guess = input("Guess a number (1-100) > ")
        params = {"guess": guess}
        r = requests.get("http://localhost:1337/api/guess_the_number", params=params) # and to get the game data about the current guess, send a get request to http://localhost:1337/api/guess_the_number
        game_data = r.json() # receive the game data (it's json, so this is why you need to parse it here)

        if game_data["win"]:
            print("YOU WIN! the number was {0}".format(guess))
            break
        elif game_data["state"] == "lower":
            print("Your number is lower, try again..")
        else:
            print("Your number is higher, try again..")
