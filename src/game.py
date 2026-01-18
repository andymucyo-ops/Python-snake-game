
class Game:

    def __init__(self,height: int,width: int) -> None:
        self.height = height
        self.width = width

    def board_matrix(self):
        empty_board: list[list] = []

        for line in range(self.height):
            empty_line: list = []
            
            for col in range(self.width):
                empty_line.append(None)

            empty_board.append(empty_line)    

        
        # print(f'Hight: {self.height}')
        # print(f'Width: {self.width}')
        return empty_board

    def render(self):

        matrix: list[list] = self.board_matrix()

        for row in range(self.height):
            # print(row)
            if row == 0 or row == self.height - 1:
               # print(f'{row} begin/end row')

               for col in range(self.width):
                    if col == 0 or col == self.width - 1: 
                        matrix[row][col] = "+"
                        # print(f'{col} begin,end')
                    else: 
                        matrix[row][col] = "-"
                        # print(f'{col} middle col')
                    # else: 
                        # matrix[row][col] = "+"

            else: 
               # print(f'{row} middle row')

               for col in range(self.width):
                    if col == 0 or col == self.width - 1: 
                        matrix[row][col] = "|"
                        # print(f'{col} begin,end')
                    else:
                        matrix[row][col] = " "
                        # print(f'{col} middle col')
                    # else:
                    #     matrix[row][col] = "+"
        return matrix
    
    def display_print(self):

        board: list[list] = game.render()

        for line in board:
            for col in line:
                print(col, end='')
            print('')



if __name__ == '__main__' :
    
    game = Game(8,16)
    game.display_print()
