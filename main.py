class BaseCharater():
    def __init__(self, name: str, pos_x: int, pos_y: int,
                 is_live: bool) -> None:
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_live = is_live
    
    def __str__(self) -> str:
        return self.name + ' ' + str(self.is_live)
    
    def __repr__(self) -> str:
        return self.name
