import random
from typing import List, Dict


def avoid_my_neck(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:

    my_neck = my_body[1]  # The segment of body right after the head is the 'neck'

    if my_neck["x"] < my_head["x"]:  # my neck is left of my head
        possible_moves.remove("left")
    elif my_neck["x"] > my_head["x"]:  # my neck is right of my head
        possible_moves.remove("right")
    elif my_neck["y"] < my_head["y"]:  # my neck is below my head
        possible_moves.remove("down")
    elif my_neck["y"] > my_head["y"]:  # my neck is above my head
        possible_moves.remove("up")

    return possible_moves

def build_board(board):
    b = [[0 for x in range(board['width'])] for y in range(board['height'])]
    for snake in board['snakes']:
        for body in snake['body']:
            b[body['x']][body['y']] = 1
    for food in board['food']:
        b[food['x']][food['y']] = 2
    return b

def is_move_safe(x, y, board):
    if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
        return False
    return board[x][y]!=1

def distance(x1, y1, x2, y2):
    return ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

def nearest_food(x, y, board):
    minDist = 9223372036854775807
    currFood = None
    for food in board['food']:
        d = distance(x, y, food['x'], food['y'])
        if d < minDist:
            minDist = d
            currFood = food
    return currFood, minDist

def get_safe_moves(x, y, board):
    r = []
    if is_move_safe(x, y+1, board):
        r.append("up")
    if is_move_safe(x, y-1, board):
        r.append("down")
    if is_move_safe(x+1, y, board):
        r.append("right")
    if is_move_safe(x-1, y, board):
        r.append("left")
    return r

def get_pref_direction(x, y, dest):
    if x > dest['x']:
        return "left"
    elif x < dest['x']:
        return "right"
    elif y < dest['y']:
        return "up"
    return "down"


def choose_move(data: dict) -> str:
    my_head = data["you"]["head"]
    x = my_head['x']
    y = my_head['y']
    my_body = data["you"]["body"]

    board = build_board(data['board'])

    health = data['you']['health']

    cF, minDist = nearest_food(x, y, data['board'])

    pref = ""
    if cF:
        if health <= minDist + 5:
            pref = get_pref_direction(x, y, cF)
    
    safe_moves = get_safe_moves(my_head['x'], my_head['y'], board)

    if pref in safe_moves:
        move = pref
    else:
        move = random.choice(safe_moves)

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {safe_moves}")

    return move
