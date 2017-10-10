class Grid:
    '''Grid Class'''

    # directions of ant after hitting white or black square
    dirs_wh = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}
    dirs_bl = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    dirs_ant = {'N': [0, -1], 'E': [1, 0], 'S': [0, 1], 'W': [-1, 0]}

    def __init__(self, w, h):
        '''Init Grid object with width and height'''
        self.w = w
        self.h = h
        self.grid = []

    def set_Ant(self, ant_x, ant_y, ant_dir):
        '''Set ant initial position x, y and direction'''
        self.ant_x = ant_x
        self.ant_y = ant_y
        self.ant_dir = ant_dir

    def read_grid(self):
        '''Read grid data from input'''
        for _ in range(self.w):
            self.grid.append(list(input()))

    def next_state(self, t=1):
        '''Calculate next t states of Grid'''
        for _ in range(t):
            col = self.grid[self.ant_y][self.ant_x]
            if col == '.':
                self.ant_dir = self.dirs_wh[self.ant_dir]
                self.grid[self.ant_y][self.ant_x] = '#'
            else:
                self.ant_dir = self.dirs_bl[self.ant_dir]
                self.grid[self.ant_y][self.ant_x] = '.'
            n_pos = self.dirs_ant[self.ant_dir]
            self.ant_x += n_pos[0]
            self.ant_y += n_pos[1]

    def prnt(self):
        '''Print method for CodinGame output.
        __str__() for some reasons doesn`t work xD'''
        for x in self.grid:
            print(*x, sep='')

    def __str__(self):
        s = ''
        for x in self.grid:
            s += ''.join(x)
            s += '\n'
        return s


w, h = [int(i) for i in input().split()]
Plansza = Grid(w, h)

x, y = [int(i) for i in input().split()]
direction = input()
Plansza.set_Ant(x, y, direction)

t = int(input())

Plansza.read_grid()
Plansza.next_state(t)
Plansza.prnt()
