import numpy as np

#if it is a valid places to any player it will return all states and its sucessors it will be earned else it will return null
def decide_place(color , board):
    validMoves = {}
    validParts = {}
    valid = 0
    for x in range(8):
        for y in range(8):
            place = [x , y]

            income = isv(board, color, place)

            if len(income) > 0:
                #print  place
                #validMoves[valid] = place
                validParts[valid] = income
                valid += 1
    return validMoves , validParts , valid

    #detrmine weather the place is on table or not
def isOntabel(place):
    return place[0] >= 0 and place[0] <= 7 and place[1] >= 0 and place[1] <= 7

    #detrimne if the move is valid or not and if it is vlid it returns the places which will be turned else it will return false
# def isValidMove(board , color , place):
#     validMoves = []
#
#     if color == 'W':
#         othercolor = 'B'
#     else:
#         othercolor = 'W'
#     copyOfPlace = place
#
#     for x, y in [[1, 0], [-1, 0], [-1, -1], [0, -1], [1, -1], [-1, 1], [0, 1], [1, 1]]:
#         xstart, ystart = x , y
#         copyOfPlace[0] = copyOfPlace[0] + x
#         copyOfPlace[1] = copyOfPlace[1] + y
#         if not isOntabel(copyOfPlace):
#             continue
#         # There is a other color here that may be earned
#         if board[copyOfPlace[0]][copyOfPlace[1]].Color == othercolor:
#             copyOfPlace[0] = copyOfPlace[0] + x
#             copyOfPlace[1] = copyOfPlace[1] + y
#             if not isOntabel(copyOfPlace):
#                 continue
#             while board[copyOfPlace[0]][copyOfPlace[1]].Color == othercolor:
#
#                 copyOfPlace[0] = copyOfPlace[0] + x
#                 copyOfPlace[1] = copyOfPlace[1] + y
#                 #print copyOfPlace
#
#                 if not isOntabel(place):
#                     continue
#             if not isOntabel(copyOfPlace):
#                 continue
#             #There is a other color here that will be earned
#             if board[copyOfPlace[0]][copyOfPlace[1]].Color == color:
#
#                 while True:
#                     copyOfPlace[0] = copyOfPlace[0] - x
#                     copyOfPlace[1] = copyOfPlace[1] - y
#                     if x == xstart and y == ystart:
#                         break
#                     validMoves.append(copyOfPlace)
#     return validMoves

def isv(board , color , place):
    valid = []
    if color == 'W':
        othercolor = 'B'
    else:
        othercolor = 'W'

    copyOfPlace = list(place)
    for x, y in [[1, 0], [-1, 0], [-1, -1], [0, -1], [1, -1], [-1, 1], [0, 1], [1, 1]]:
        xstart, ystart = x , y
        copyOfPlace[0] = copyOfPlace[0] + x
        copyOfPlace[1] = copyOfPlace[1] + y
        #print copyOfPlace
        if not isOntabel(copyOfPlace):
            continue
        while board[copyOfPlace[0]][copyOfPlace[1]].Color == othercolor:
            copyOfPlace[0] = copyOfPlace[0] + x
            copyOfPlace[1] = copyOfPlace[1] + y
            print place ,  copyOfPlace

        if board[copyOfPlace[0]][copyOfPlace[1]].Color == color:
            while x >= xstart and y >= ystart:
                copyOfPlace[0] = copyOfPlace[0] - x
                copyOfPlace[1] = copyOfPlace[1] - y
                valid.append(list(copyOfPlace))

        copyOfPlace = list(place)
    return valid


#return state of states
def Minimax(color, board):
    validList = decide_place(color , board)[0]
    valid_List = validList.values()
    theminimax_values = []

    for i in valid_List:
        score = []
        the_highest_score = getComputerPlay(board, color, i, score, 0)
        theminimax_values.append([i, the_highest_score])
    maxx = -100

    for i in theminimax_values:
        if i[1] > maxx:
            maxx = i[1]
            node = i[0]
    return node

def getComputerPlay(board, color, place, score, counter):
    # score is empty list passed so that we can collect all the scores of all cases
    v_board = board
    if color == "W":
        v_board[place[0]][place[1]] = 'W'
        revColor = "B"
    else:
        v_board[place[0]][place[1]] = 'B'
        revColor = "W"

    if iswon(v_board) == None:  # no won wins
        dict = decide_place(v_board, revColor)
        list = []

        for key in dict:
            element = []
            indeces = dict[key]  # this list carry the index of the available places
            element.append(indeces[0])
            element.append(indeces[1])
            list.append(element)

        if counter == 3:
            return score
        else:
            for choice in list:
                getComputerPlay(v_board, revColor, choice, counter)

        counter = counter + 1
    # if either of them wins returns the score
    else:
        score.append(getScore(v_board))
    return max(score)

def get_score_by_place(place):
    Places = np.array([ [1000,   50,  100,  100,  100,  100,   50, 1000,], # P[0][0], P[0][1], ..., P[0][7]
                 [  50,  -20,  -10,  -10,  -10,  -10,  -20,   50,], # P[1][0], P[1][1], ..., P[1][7]
                 [ 100,  -10,    1,    1,    1,    1,  -10,  100,], # P[2][0], P[2][1], ..., P[2][7]
                 [ 100,  -10,    1,    1,    1,    1,  -10,  100,], # P[3][0], P[3][1], ..., P[3][7]
                 [ 100,  -10,    1,    1,    1,    1,  -10,  100,], # P[4][0], P[4][1], ..., P[4][7]
                 [ 100,  -10,    1,    1,    1,    1,  -10,  100,], # P[5][0], P[5][1], ..., P[5][7]
                 [  50,  -20,  -10,  -10,  -10,  -10,  -20,   50,], # P[6][0], P[6][1], ..., P[6][7]
                 [1000,   50,  100,  100,  100,  100,   50, 1000,],])# P[7][0], P[7][1], ..., P[7][7]
    return Places[place[0] , place[1]]

def get_all_weighted_score(board):
    white , black = 0 , 0
    for i in range(8):
        for j in range(8):
            if board[i][j].color == 'W':
                white += 1
            elif board[i][j].color == 'B':
                black += 1
    return white , black

def getScore(board):
    black , white = get_all_weighted_score(board)
    return black - white

def iswon(board):
    sblack, Empty, swhite = 0, 0, 0
    for i in xrange(len(board)):
        for j in xrange(len(board[i])):
            if (board[i][j] != 'E'):
                if (board[i][j] == 'W'):
                    swhite += 1
                else:
                    sblack += 1
            else:
                Empty += 1
    # print Empty , sblack , swhite
    if (swhite != 0 and sblack == 0):  # lw mafe4 wla wa7da soda w fe abyad  return el abyad
        player = "W"
        return player
    elif (sblack != 0 and swhite == 0):  # lw mafe4 wla wa7da beda w fe aswed  return el aswed
        player = "B"
        return player
    elif (Empty == 0):  # lw mafe4 wla wa7da fadia
        if (sblack > swhite):  # lw el aswed  aktr return el eswed
            player = "B"
            return player
        else:  # lw el abyad  aktr return el abyad
            player = "W"
            return player
    else:
        return None  # lw fe abyad w eswed w fady  yb2a m7ade4 ksb
