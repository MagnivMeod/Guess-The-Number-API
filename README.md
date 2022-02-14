# Guess-The-Number-API
Create your own guess the number game by using this API!
This API is an open source API so you can download and do different things with it or just use it as it is.

# API Reference

API Endpoint: "http://localhost:1337/api"

API Get start game: "http://localhost:1337/api/start_game"

API Get game data: "http://localhost:1337/api/guess_the_number"

params: "guess" - is the guess number

game data: "win"   - is the boolean value that tells if player wins or not (True / False)

game data: "state" - is the state of the guess number, can receive 3 values; "lower", "higher", "equals".

# How To Use
To find out how to use, view code example on file "client.py".

# Notice
Make sure you run the API Server before you run the client
