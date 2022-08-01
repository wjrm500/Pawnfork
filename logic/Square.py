from statistics import mean
from string import ascii_lowercase

class Square:
    def __init__(self, file, rank) -> None:
        self.file = file
        self.rank = rank
        self.file_name = ascii_lowercase[self.file - 1]
        self.rank_name = str(self.rank)
        self.set_geometry()
        self.piece = None
    
    def __repr__(self) -> str:
        return f'{self.file}{self.rank}'
    
    def set_geometry(self):
        self.x_min = self.file - 1
        self.x_max = self.file
        self.y_min = 9 - self.rank - 1
        self.y_max = 9 - self.rank
        self.x_centre = mean([self.x_min, self.x_max])
        self.y_centre = mean([self.y_min, self.y_max])
        self.centre = (self.x_centre, self.y_centre)
    
    def set_piece(self, piece):
        self.piece = piece