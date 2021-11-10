import random
class tic_tac_toe():
    def __init__(self,board):
        self.board=board

    def display_board(self):
        print("\n*100")

        print('  |  |')
        print(' '+ self.board[7] + '|' +self.board[8] + ' |' + self.board[9])
        print('  |  |')
        print('-----------')
        print('  |  |')
        print(' '+ self.board[4] + '|' +self.board[5] + ' |' + self.board[6])
        print('  |  |')
        print('-----------')
        print('  |  |')
        print(' '+ self.board[1] + '|' +self.board[2] + ' |' + self.board[3])
        print('  |  |')


    def player_input(self):
        marker=""
        while not(marker=="X" or marker=="O"):
            marker=input("Player 1: Do you want to be X or O? ").upper()

        if marker == "X":
            return ("X","O")
        else:
            return("O","X")

    def place_marker(self,marker,position):
        self.board[position]=marker


    def win_check(self,mark):
        return ((self.board[7] == mark and self.board[8] == mark and self.board[9] == mark) or
    (self.board[4] == mark and self.board[5] == mark and self.board[6] == mark) or
    (self.board[1] == mark and self.board[2] == mark and self.board[3] == mark) or
    (self.board[7] == mark and self.board[4] == mark and self.board[1] == mark) or
    (self.board[8] == mark and self.board[5] == mark and self.board[2] == mark) or
    (self.board[9] == mark and self.board[6] == mark and self.board[3] == mark) or
    (self.board[7] == mark and self.board[5] == mark and self.board[3] == mark) or
    (self.board[9] == mark and self.board[5] == mark and self.board[1] == mark)) 


    def choose_first(self):
        if random.randint(0,1)==0:
            return "player 2"
        else:
            return "player 1"

    def space_check(self,position):
        return self.board[position]==" "

    def full_board_check(self):
        for i in range(1,10):
            if self.space_check(i):
                return False
        return True   

    def player_choice(self):
        position=0

        while position not in [1,2,3,4,5,6,7,8,9] or not self.space_check(position):
            position=int(input("choose your next position(1-9): "))

        return position

    def replay(self):
        return input("do you want to play again? Enter Yes or No: ").lower().startswith('y')


if __name__=="__main__":
    print("welcome to tic tac toe!")

    while True:
        theboard=[" "]*10
        game=tic_tac_toe(theboard)
        player1_marker, player2_marker=game.player_input()
        turn=game.choose_first()
        print(turn + ' will go first.')

        play_game= input("Are you ready to play ? Enter Yes or No.")

        if play_game.lower()[0]=="y":
            game_on=True
        else:
            game_on=False

        while game_on:
            if turn == "player 1":
                game.display_board()
                position=game.player_choice()
                game.place_marker(player1_marker,position)

                if game.win_check(player1_marker):
                    game.display_board()
                    print('Congratulations ! You have won the game!')

                    game_on=False

                else:
                    if game.full_board_check():
                        game.display_board()
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'player 2'                    
            else:
                game.display_board()
                position=game.player_choice()
                game.place_marker(player2_marker,position)

                if game.win_check(player2_marker):
                    game.display_board()
                    print('Player 2 has won!')
                    game_on=False

                else:
                    if game.full_board_check():
                        game.display_board()
                        print('The game is a draw!')
                        break

                    else:
                        turn = 'player 1'

        if not game.replay():
            break                    

