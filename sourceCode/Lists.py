
class Grid:
    def __init__(self, width, height):
        self.squares = []
        for i in range(height):
            self.squares.append([])