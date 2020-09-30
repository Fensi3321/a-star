class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [self.__zero_row(width) for i in range(height)]

    def __zero_row(self, width):
        return [0 for i in range(width)]

    def print_grid(self):
        for x in self.grid:
            print(x)
'''
[
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]
'''