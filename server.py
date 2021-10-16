import logging
import os

from flask import Flask
from flask import request

import server_logic


app = Flask(__name__)
import collections

def print_odict(odict, depth=0, name=""):
    if type(odict) == str or type(odict) == int:
        print("{}{}".format("   " * depth, odict))
    elif type(odict) == list or type(odict) == tuple:
        for i in range(len(odict)):
            if type(odict[i]) == str or type(odict[i]) == int:
                print("{}{}[{}] = {}".format("   " * (depth), name, i, odict[i]))
            else:
                print("{}{}[{}]".format("   " * (depth), name, i))
                print_odict(odict[i], depth+1)
    elif type(odict) == collections.OrderedDict or type(odict) == dict:
        for key in odict.keys():
            if type(odict[key]) == list or type(odict[key]) == dict or type(odict[key]) == collections.OrderedDict:
                print("{}{}[{}]".format("   " * depth, name, key))
                print_odict(odict[key], depth+1)
            else:
                print("{}{}[{}] = {}".format("   " * depth, name, key, odict[key]))


@app.get("/")
def handle_info():
    print("INFO")
    return {
        "apiversion": "1",
        "author": "Hissnake",  # TODO: Your Battlesnake Username
        "color": "#11CCDD",  # TODO: Personalize
        "head": "default",  # TODO: Personalize
        "tail": "default",  # TODO: Personalize
    }


@app.post("/start")
def handle_start():
    data = request.get_json()

    print_odict(data)

    return "ok"


@app.post("/move")
def handle_move():
    data = request.get_json()

    #print_board(data['board'])

    # TODO - look at the server_logic.py file to see how we decide what move to return!
    move = server_logic.choose_move(data)

    return {"move": move}

def print_board(board):
    s = [[" " for x in range(board['width'])] for y in range(board['height'])]
    for snake in board['snakes']:
        c = snake['name'][:1]
        for body in snake['body']:
            s[body['y']][body['x']] = c
    for x in s:
        l = ""
        for y in x:
            l += "[{}]".format(y)
        print(l)

@app.post("/end")
def end():
    data = request.get_json()

    print(f"{data['game']['id']} END")
    return "ok"


if __name__ == "__main__":
    logging.getLogger("werkzeug").setLevel(logging.ERROR)

    print("Starting Battlesnake Server...")
    app.run(host="0.0.0.0")
