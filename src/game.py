from snake import Snake, UP 


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
          
        for position in self.snake:
            if position == self.snake.head():
                matrix[self.snake.head()[0]][self.snake.head()[1]] = "X"
            else:
                matrix[position[0]][position[1]] = "O"


        return matrix
    
    def display_print(self) -> None:

        board: list[list] = game.render()

        for line in board:
            for col in line:
                print(col, end='')
            print('')

        



if __name__ == '__main__' :
    
    game = Game(16,32)

    game.display_print()
