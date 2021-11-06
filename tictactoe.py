print("Welcome to the my first 'tic-tac-toe' game.")
Board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
                '1': ' ' , '2': ' ' , '3': ' ' }
Board_keys = []

for key in Board:
    Board_keys.append(key)


def print_Board(Board):
    print(Board['7'] + '|' + Board['8'] + '|' + Board['9'])
    print('-+-+-')
    print(Board['4'] + '|' + Board['5'] + '|' + Board['6'])
    print('-+-+-')
    print(Board['1'] + '|' + Board['2'] + '|' + Board['3'])
   
def game():

    turn = "X"
    count = 0
    for i in range(0,10):
        print_Board(Board)
        print("Your turn " + turn + " Select a spot please.")

        move = input()

        if Board[move] == " ":
            Board[move] = turn
            count += 1
        else:
            print("This spot is already filled. Move to which spot?")
            continue
        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ': 
                print("Game Over.")                
                print(" --- " +turn + " won. ---")                
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ': 
                print_Board(Board)
                print("Game Over.")                
                print(" --- " +turn + " won. ---")
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ': 
                print_Board(Board)
                print("Game Over.")                
                print(" --- " +turn + " won. ---")
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ': 
                print_Board(Board)
                print("Game Over.")                
                print(" --- " +turn + " won. ---")
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ': 
                print_Board(Board)
                print("Game Over.")                
                print(" --- " +turn + " won. ---")
                break
            elif Board['3'] == Board['6'] == Board['9'] != ' ': 
                print_Board(Board)
                print("Game Over.")                
                print(" --- " +turn + " won. ---")
                break 
            elif Board['7'] == Board['5'] == Board['3'] != ' ': 
                print_Board(Board)
                print("Game Over.")                
                print(" --- " +turn + " won. ---")
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ': 
                print_Board(Board)
                print("Game Over.")                
                print(" --- " +turn + " won. ---")
                break 
        if count == 9:
             print("It's a tie.")
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    restart=input("Wanna play again? |Y or N|")
    if restart == "y" or restart == "Y":
        for key in Board_keys:
            Board[key] = " "

        game()

if __name__ == '__main__':
    game()
