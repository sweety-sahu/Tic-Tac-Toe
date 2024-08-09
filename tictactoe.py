def tictactoe(val):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8]))
    print("\t     |     |")
    print("\n")
 
def myscore_board(score_board):
    print("\t********************************")
    print("\t         SCORE BOARD       ")
    print("\t********************************")
 
    list_of_players = list(score_board.keys())
    print("\t   ", list_of_players[0], "\t    ", score_board[list_of_players[0]])
    print("\t   ", list_of_players[1], "\t    ", score_board[list_of_players[1]])
 
    print("\t********************************\n")
 
def check_Victory(playerposition, current_player):
 
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    for i in solution:
        if all(k in playerposition[current_player] for k in i):
 
            return True


    return False      
 
def check_Tie(playerposition):
    if len(playerposition['X']) + len(playerposition['O']) == 9:
        return True
    return False      
 
def singlegame(current_player):
 
    val = [' ' for i in range(9)]
     
    playerposition = {'X' : [], 'O' : []}
     
    while True:
        tictactoe(val)
         
        try:
            print(current_player, "'s turn. Choose the Block for your turn : ", end="")
            chance = int(input())
        except ValueError:
            print("Invalid Input!!! Try Again")
            continue


        if chance < 1 or chance > 9:
            print("Wrong Input!!! Please Try Again")
            continue
 
        if val[chance - 1] != ' ':
            print("Wrong Input!!! Please Try Again")
            continue
        val[chance - 1] = current_player
 
        playerposition[current_player].append(chance)


        if check_Victory(playerposition, current_player):
            tictactoe(val)
            print("Congrats!", current_player, " has won!!")    
            print("\n")
            return current_player


        if check_Tie(playerposition):
            tictactoe(val)
            print("Tie")
            print("\n")
            return 'D'


        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


if __name__ == "__main__":


    print("First Player")
    FirstPlayer = input("Name: ")
    print("\n")


    print("Second Player")
    SecondPlayer = input("Name: ")
    print("\n")


    current_player = FirstPlayer
 
    playerchoice = {'X' : "", 'O' : ""}
 
    opt = ['X', 'O']
 
    score_board = {FirstPlayer: 0, SecondPlayer: 0}
    myscore_board(score_board)
 
    while True:
 
        print(current_player, "will make the choice:")
        print("Press 1 for X")
        print("Press 2 for O")
        print("Press 3 to Quit")
 
        try:
            the_choice = int(input())  
        except ValueError:
            print("Invalid Input!!! Try Again\n")
            continue
 
        if the_choice == 1:
            playerchoice['X'] = current_player
            if current_player == FirstPlayer:
                playerchoice['O'] = SecondPlayer
            else:
                playerchoice['O'] = FirstPlayer
 
        elif the_choice == 2:
            playerchoice['O'] = current_player
            if current_player == FirstPlayer:
                playerchoice['X'] = SecondPlayer
            else:
                playerchoice['X'] = FirstPlayer
         
        elif the_choice == 3:
            print("The Final Scores")
            myscore_board(score_board)
            break  
 
        else:
            print("Try Again\n")
 
        win = singlegame(opt[the_choice - 1])
     
        if win != 'D' :
            playerWon = playerchoice[win]
            score_board[playerWon] = score_board[playerWon] + 1
 
        myscore_board(score_board)
        if current_player == FirstPlayer:
            current_player = SecondPlayer
        else:
            current_player = FirstPlayer
