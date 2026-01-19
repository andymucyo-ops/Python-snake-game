# direction tuple[int]s
UP: tuple[int] = (0,1)
DOWN: tuple[int] = (0,-1)
LEFT: tuple[int] = (-1,0)
RIGHT: tuple[int] = (1,0) 

#class definition
class Snake:
    def __init__(self, body: list[tuple[int]], direction: tuple[int]) -> None:
        self.body = body
        self.direction = direction
    
    def __iter__(self):
        return iter(self.body)

    def move(self, position: tuple[int]) -> list[tuple[int]]:
        self.body = self.body[1:].append(position) 
    
    def set_direciton(self, direction: tuple[int]) -> None:
        self.direction = direction

    def head(self) -> tuple[int]:

        return self.body[-1]


