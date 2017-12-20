
def getComputerPlay(board, color, place, score): # score is empty list passed so that we can collect all the scores of all cases
    v_board = board
    if color == "white":
        v_board[place[0]][place[1]] = 'white'
        revColor = "black"
    else :
        v_board[place[0]][place[1]] = 'black'
        revColor = "white"

    if isWon(v_board) == None: # no won wins
        dict = decidePlaces(v_board, revColor)
        list = []

        for key in dict :
            element = []
            indeces = dict[key] # this list carry the index of the available places
            element.append(indeces[0])
            element.append(indeces[1])
            list.append(element)

        for choice in list:
            getComputerPlay(v_board, revColor, choice)

    else: # if either of them wins returns the score
        score.append(getScore())
        return score
