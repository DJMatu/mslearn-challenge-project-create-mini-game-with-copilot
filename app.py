# Make the logic of the game "rock, paper scissors" to play in console in multiplayer mode

# Create a list of possible moves
moves = ['rock', 'paper', 'scissors']



# Create a function that check if the data inputted is in the list of moves
def check_move(move):
    if move not in moves:
        print('Invalid move')
        return False
    else:
        return True

# create a function that identifies the winner
def identify_winner(player1_move, player2_move):
    global player1wins
    global player2wins
    global draw
    if player1_move == player2_move:
        draw += 1
        return 'draw'
    elif player1_move == 'rock' and player2_move == 'scissors':
        player1wins += 1
        return 'Player ' + player1 + ' win'
    elif player1_move == 'paper' and player2_move == 'rock':
        player1wins += 1
        return 'Player ' + player1 + ' win'
    elif player1_move == 'scissors' and player2_move == 'paper':
        player1wins += 1
        return 'Player ' + player1 + ' win'
    else:
        player2wins += 1
        return 'Player ' + player2 + ' win'
        


def play():
    global player1wins
    global player2wins
    global draw
    player1_move = input("Enter your move"+ player1+' :  ')
    while check_move(player1_move) == False:
        player1_move = input("Enter your move"+ player1+' :  ')

    player2_move = input("Enter your move" + player2+' :  ')
    while check_move(player2_move) == False:
        player2_move = input("Enter your move"+ player2+' :  ')

    identify_winner(player1_move, player2_move)
    print('Player1: ' + str(player1wins) +',   Player2: ' + str(player2wins)  + '  Draw: '+ str(draw))

    play_again = input('Do you want to play again? (yes/no)':  )
    if play_again == 'yes':
        play()
    else:
        exit()

def exit():
    print('Game over')
    print('Player1: ' + str(player1wins) +',   Player2: ' + str(player2wins) + '  Draw: '+ str(draw))
    if player1wins > player2wins:
        print(player1+' wins')
    elif player1wins < player2wins:
        print(player2+' wins')
    else:
        print('Draw')


start = input('Do you want to play? (yes/no):   ')
if start == 'yes':
    player1 = input('Enter your name Player1:  ')
    player2 = input('Enter your name Player2:  ')
    player1wins = 0
    player2wins = 0
    draw = 0
    play()
else:
    exit()

