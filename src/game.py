
import os 
from .snake import Snake, UP, DOWN, LEFT, RIGHT


class Game:

    def __init__(self,height: int,width: int) -> None:
        self.height = height
        self.width = width
        self.snake: list[tuple[int]] = Snake([(9,15), (8,15), (7,15), (7,16), (6,16), (5,16)], UP)

    def board_matrix(self) -> list[list]:
        empty_board: list[list] = []

        for line in range(self.height):
            empty_line: list = []
            
            for col in range(self.width):
                empty_line.append(None)

            empty_board.append(empty_line)    

        return empty_board

    def render(self) -> list[list[str]]:

        matrix: list[list] = self.board_matrix()

        snake: Snake = self.snake 

        for row in range(self.height):
            
            if row == 0 or row == self.height - 1:
               
               for col in range(self.width):
                    if col == 0 or col == self.width - 1: 
                        matrix[row][col] = "+"
                        
                    else:
                        matrix[row][col] = "-"

            else: 

               for col in range(self.width):
                    if col == 0 or col == self.width - 1: 
                        matrix[row][col] = "|"
           
                    else:
                        matrix[row][col] = " "
        
        for position in snake.body:
            if position == snake.head():
                matrix[snake.head()[0]][snake.head()[1]] = "X"
            
            else:
                matrix[position[0]][position[1]] = "O"


        return matrix
    
    def display_print(self) -> None:

        board: list[list[str]] = self.render()

        for row in board:
            for col in row:
                print(col, end='')
            print('')

        
    def player_interaction(self) -> None:
        moves: dict[str,str] = {'w':UP, 's':DOWN, 'a':LEFT, 'd':RIGHT}

        snake: Snake = self.snake 

        game: Game = self

        # print(f'first snake position is {snake.body}')

        player_input: str = input("Please enter your move (w = UP, s = DOWN, a = LEFT, d = RIGHT: ").lower()

        while True:
        
            if player_input not in moves.keys():
                if player_input == "":

                    os.system("clear")
                    game.display_print()
                    # game.player_interaction()
                    player_input: str = input("Next move: ")

                else:

                    print("Please enter w, a, s or d to move!")

                    player_input: str = input("Please enter your move (w = UP, s = DOWN, a = LEFT, d = RIGHT: ").lower()

                    os.system("clear")
                    game.display_print()

        
            else:
                x_coordinate: int = snake.head()[0] + moves[player_input][0]
                y_coordinate: int = snake.head()[1] + moves[player_input][1]
                head_position: tuple[int] = (x_coordinate,y_coordinate)

                # print(f'new position is {head_position}')

                self.snake = Snake(snake.move(head_position),moves[player_input]) 

                os.system("clear")
                game.display_print()

                # game.player_interaction()

                player_input: str = input("Next move: ")





if __name__ == '__main__' :
    
    game = Game(16,32)

    game.display_print()

    game.player_interaction()
