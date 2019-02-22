import pprint

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

#establish coordinates for the board via dictionary
#the key is the coordinate, and the value would be either X, O, or blank(empty string)

def drawBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    #top section
    print('-+-+-')
    #divider
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    #middle section
    print('-+-+-')
    #divider
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    #bottom section


drawBoard(board)

def movesAvailable(x):
    print('The moves available are: ')
    #tells the player what moves are available
    for k, v in x.items():
        if v == ' ':
            #if the value is ' ' then the move is available, so print the key
            pprint.pprint(k)


player = 'X'
#establish which players turn it is:
spaces = board
#use spaces to be able to delete keys without affecting the board
for i in range(0,9):
    print('It is currently player ' + player + "'s turn.")
    #tell the player whos turn it is
    movesAvailable(spaces)
    #check to see what moves are available
    move = input('Player ' + player + ', which space would you like to play? ')
    #ask the player where to put the marker
    del spaces[move]
    #remove the move from the list of available moves
    board[move] = player
    #place the marker on the board inthe move position
    if player == 'X':
        player = '0'
        #if it was player 'X's turn, change
    else:
        player = 'O'
        #if it was player 'O's turn, change
    drawBoard(board)
    #reDraw the board
    



    
