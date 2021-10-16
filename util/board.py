

# 0 = empty
# 1 = food
# 2 = me
# 3 = enemy

def get_board(data):
    board = data['board']
    return_board = [[0 for x in range(board['width'])] for y in range(board['height'])]
    
    for snake in board['snakes']:
        for body in snake['body']:
            return_board[body['x']][body['y']] = 3
    for food in board['food']:
        b[food['x']][food['y']] = 1
    for body in data['you']:
        return_board[body['x']][body['y']] = 2
        
    return return_board
    

def get_heatmap(board):
    return [][]
