board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def isGameOver(board):
    # across horizontal spaces
    return ((board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X') or
       (board['top-L'] == 'O' and board['top-M'] == 'O' and board['top-R'] == 'O') or
       (board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R'] == 'X') or
       (board['mid-L'] == 'O' and board['mid-M'] == 'O' and board['mid-R'] == 'O') or
       (board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X') or
       (board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == 'O') or
       # across vertical spaces
       (board['top-L'] == 'X' and board['mid-L'] == 'X' and board['low-L'] == 'X') or
       (board['top-L'] == 'O' and board['mid-L'] == 'O' and board['low-L'] == 'O') or
       (board['top-M'] == 'X' and board['mid-M'] == 'X' and board['low-M'] == 'X') or
       (board['top-M'] == 'O' and board['mid-M'] == 'O' and board['low-M'] == 'O') or
       (board['top-R'] == 'X' and board['mid-R'] == 'X' and board['low-R'] == 'X') or
       (board['top-R'] == 'O' and board['mid-R'] == 'O' and board['low-R'] == 'O') or
       # across diagonals
       (board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R'] == 'X') or
       (board['top-L'] == 'O' and board['mid-M'] == 'O' and board['low-R'] == 'O') or
       (board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-L'] == 'X') or
       (board['top-R'] == 'O' and board['mid-M'] == 'O' and board['low-L'] == 'O'))

turn = 'X'
i = 0
print('===========TIC TAC TOE===========')
print('Note: You must enter one of the following positions in each move : ')
for i in board.keys():
    print(i)
print('---------------------------------')
print('Let\'s begin the game!!')
while i < 9:
    printBoard(board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    # for invalid moves
    if move not in board.keys():
        print('Please enter a valid position!')
    elif board[move] != ' ':
        print('This space is already filled! Enter another position')
    else:
        i+=1
        board[move] = turn
        result = isGameOver(board)
        if result == True:
            printBoard(board)
            print('The game is over! The winner is player ' + turn);
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
else:
    printBoard(board)
    print('The game is over! It is a tie!')
