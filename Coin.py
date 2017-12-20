class Coin():
    Color = 'E'
    place = [2]

board = [[0 for x in range(8)] for y in range(8)]
for  i in range(8):
    for j in range(8):
        board[i][j] = Coin()
        board[i][j].place = [i , j]

board[4][4].Color = 'B'
board[4][3].Color = 'W'
board[3][4].Color = 'B'
board[3][3].Color = 'W'