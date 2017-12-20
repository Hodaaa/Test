#--------------------- Function   who is winner ? ------------------------------- #
#this is function return winner if exist else  return none  let's see

def iswon(board):
    sblack ,Empty, swhite = 0 , 0 , 0
    for i in xrange(len(board)):
        for j in xrange(len(board[i])):
            if (board[i][j] != 'E'):
                if(board[i][j] == 'W'):
                    swhite += 1
                else :
                    sblack += 1
            else:
                Empty += 1
    # print Empty , sblack , swhite
    if (swhite != 0 and sblack == 0 ): # lw mafe4 wla wa7da soda w fe abyad  return el abyad
        player = "W"
        return player
    elif (sblack != 0 and swhite == 0 ): # lw mafe4 wla wa7da beda w fe aswed  return el aswed
        player = "B"
        return player
    elif (Empty == 0 ) :   # lw mafe4 wla wa7da fadia
        if(sblack > swhite):  # lw el aswed  aktr return el eswed
            player = "B"
            return player
        else :             # lw el abyad  aktr return el abyad
            player = "W"
            return player
    else :
        return None    # lw fe abyad w eswed w fady  yb2a m7ade4 ksb
########################################### TRACE ################################################
# b = [['E','E','E','E','B'],['B','E','E','B','B']]
# print iswon(b)