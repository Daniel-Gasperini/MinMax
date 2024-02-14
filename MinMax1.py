import time

class Isolation:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        # Initialize the game board with numbered positions
        self.current_state = [['1','2','3'],
                              ['4','5','6'],
                              ['7','8','9']]

        # Player 1 places their piece
        self.place_piece(1)

        # Player 2 places their piece
        self.place_piece(2)

        # Player 1 always plays first
        self.player_turn = 1

    def draw_board(self):
        # Draw the current game board
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    def place_piece(self, player):
        # Allow each player to place their piece on the board
        while True:
            self.draw_board()
            move = input(f'Player {player}, place your piece (1-9): ')
            if self.is_valid_move(move):
                self.make_move(move, player)
                break
            else:
                print('Invalid move! Try again.')

    def is_valid_move(self, move):
        # Check if a move is valid
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == move:
                    return True
        return False

    def make_move(self, move, player):
        # Make a move on the board
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == move:
                    self.current_state[i][j] = 'X' if player == 1 else 'O'
                    return

    def get_possible_moves(self, row, col):
        # Get all possible moves from a given position
        possible_moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 or j != 0) and 0 <= row + i < 3 and 0 <= col + j < 3:
                    if self.current_state[row + i][col + j] != 'X' and self.current_state[row + i][col + j] != 'O':
                        possible_moves.append((row + i, col + j))
        return possible_moves

    def is_end(self):
        # Check if the game has ended
        player1_moves = self.get_possible_moves(*self.get_player_position(1))
        player2_moves = self.get_possible_moves(*self.get_player_position(2))
        
        return len(player1_moves) == 0 or len(player2_moves) == 0

    def get_player_position(self, player):
        # Get the position of a player's piece on the board
        for i in range(3):
            for j in range(3):
                if self.current_state[i][j] == 'X' if player == 1 else 'O':
                    return i, j

    def play(self):
        # Main game loop
        while True:
            self.draw_board()
            self.result = self.is_end()

            # Printing the appropriate message if the game has ended
            if self.result:
                print(f'Player {3 - self.player_turn} wins!')
                break

            # If it's player's turn
            if self.player_turn == 1:
                while True:
                    current_row, current_col = self.get_player_position(1)
                    possible_moves = self.get_possible_moves(current_row, current_col)
                    move = input(f'Player 1, make your move ({possible_moves}): ')
                    if move.isdigit() and int(move) in range(1, 10):
                        move = int(move)
                        row, col = (move -1) // 3, (move - 1) % 3
                        if (row, col) in possible_moves:
                            self.make_move(str(move), 1)
                            self.player_turn = 2
                            break
                    print('Invalid move! Try again.')

            # If it's player 2's turn
            else:
                print("Player 2 is thinking...")
                time.sleep(1)
                current_row, current_col = self.get_player_position(2)
                possible_moves = self.get_possible_moves(current_row, current_col)
                move = possible_moves[0]
                self.make_move(str(move[0] * 3 + move[1] + 1), 2)
                self.player_turn = 1

def main():
    game = Isolation()
    game.play()

if __name__ == "__main__":
    main()
