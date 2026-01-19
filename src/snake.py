# direction tuple[int]s
RIGHT: tuple[int] = (0,1)
LEFT: tuple[int] = (0,-1)
UP: tuple[int] = (-1,0)
DOWN: tuple[int] = (1,0) 

#class definition
class Snake:
    def __init__(self, body: list[tuple[int]], direction: tuple[int]) -> None:
        self.body = body
        self.direction = direction

    # def body(self) -> list[tuple[int]]:
    #     return self.body()

    def __iter__(self) -> None:
        return iter(self.body)
    
    def move(self, position: tuple[int]) -> list[tuple[int]]: 
        self.body = self.body[1:]
        
        self.body.append(position) 

        return self.body
    
    # def set_direciton(self)-> None:
    #     self.direction = direction

    def head(self) -> tuple[int]:

        return self.body[-1]


