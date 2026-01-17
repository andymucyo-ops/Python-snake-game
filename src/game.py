
class Game:
    def __init__(self,height: int,width: int) -> None:
        self.height = height
        self.width = width

    def render(self):
        empty_board: list[list] = []

        for line in range(self.height):

            empty_line: list = []
            
            for col in range(self.width):
                
                empty_line.append(None)

            empty_board.append(empty_line)    
        
        print(f'Hight: {self.height}')
        print(f'Width: {self.width}')
        return empty_board


if __name__ == '__main__' :
    game = Game(4,2)

    game.render()

    print(game.render())
