from board import get_board
import printer

up    = 1
down  = 2
left  = 4
right = 8

test_board = [[0,1,0],[0,0,0],[0,0,0]]

def get_possible_moves(head, board):
    possible_moves = 15
    if head['x'] <= 0:
        possible_moves = possible_moves ^ left
    if head['x'] >= len(board) - 1:
        possible_moves = possible_moves ^ right
    if head['y'] <= 0:
        possible_moves = possible_moves ^ up
    if head['y'] >= len(board[0]) - 1:
        possible_moves = possible_moves ^ down
    return possible_moves

def test():
    results = get_possible_moves({'x':1, 'y':2}, [[0,1,0],[0,0,0],[0,0,0]])
    return_list = []
    if results & up != 0:
        return_list.append("up")
    if results & down != 0:
        return_list.append("down")
    if results & left != 0:
        return_list.append("left")
    if results & right != 0:
        return_list.append("right")
    return return_list

b = get_board()
printer.print_board(test_board)
