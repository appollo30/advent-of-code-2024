directions = {(-1,0) : "^", (1,0) : "v", (0,-1) : "<", (0,1) : ">"}

class GridMap:
    def __init__(self,input_str : str):
        lines = input_str.splitlines()
        self.n = len(lines)
        self.m = len(lines[0])
        grid = []
        for i in range(self.n):
            line = []
            for j in range(self.m):
                if lines[i][j] == '^':
                    self.position = (i,j)
                    self.direction = (-1,0)
                    line.append(".")
                elif lines[i][j] == 'v':
                    self.position = (i,j)
                    self.direction = (1,0)
                    line.append(".")
                elif lines[i][j] == '<':
                    self.position = (i,j)
                    self.direction = (0,-1)
                    line.append(".")
                elif lines[i][j] == '>':
                    self.position = (i,j)
                    self.direction = (0,1)
                    line.append(".")
                else:
                    line.append(lines[i][j])
            grid.append(line)
        self.grid = grid
        self.turns = 0
        self.visited_positions = set()

    def next_position_outside(self):
        next_position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])
        return next_position[0] < 0 or next_position[1] < 0 or next_position[0] >= self.n or next_position[1] >= self.m

    def next_position_is_obstacle(self):
        next_position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])
        return self.grid[next_position[0]][next_position[1]] == "#"

    def update(self) -> bool:
        self.visited_positions.add(self.position)
        self.turns += 1
        if self.next_position_outside():
            return False
        while self.next_position_is_obstacle():
            self.direction = (self.direction[1], -self.direction[0])
        next_position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])
        self.position = next_position
        return True

    def __str__(self) -> str:
        s = ""
        for i in range(self.n):
            for j in range(self.m):
                if (i,j) == self.position:
                    s += directions[self.direction]
                else:
                    s += self.grid[i][j]
            s += '\n'
        return s.strip()
