import random
import numpy as np
#Fill up the correct values
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4


def action_name(a):  # returns name of the action given the number assigned to it
    return "UP RIGHT DOWN LEFT".split()[a]


class IllegalAction(Exception):
    pass


class GameOver(Exception):
    pass


def compress(row):
    "remove 0s in the list"
    row1=[]
    for i in row:
        if i!=0:
            row1.append(i)
    return row1
    


def merge(row): #starts from left end, meaning swipe left
    row = compress(row)
    reward = 0
    r = [] #this is the result list after merging
    hold = -1            #one be one we pick a tile and check if mergable or not and we hold that tile here if mergable, else -1 means no tile held
    while len(row) > 0:
        v = row.pop(0)
        if hold != -1:
            if hold == v:
                reward += 2**(hold+1)
                r.append(hold + 1)
                hold = -1
            else:
                r.append(hold)
                hold = v
        else:
            hold = v
    if hold != -1: #agar after potential merges last tile still left then append it to result
        r.append(hold)
        hold = -1
    while len(r) < 4: # see at end our row should be of size 4, so if after merging size is less then this
        r.append(0)
    return reward, r


from copy import copy


class Board:
    def __init__(self, board=None):
        """board is a list of 16 integers"""
        if board is not None:  #point is that ,ki if user provides the board then keep it as is, else generate a random board
            self.board = board
        else:
            self.reset()

    def empty_tiles(self):  # returns a list of index in self.board where the value is 0
        return [i for (i, v) in enumerate(self.board) if v == 0]
    
    def reset(self):
        self.clear()
        self.board[random.choice(self.empty_tiles())] = 1
        self.board[random.choice(self.empty_tiles())] = 2

    def spawn_tile(self, random_tile=False):
        empty_tiles = self.empty_tiles()
        if len(empty_tiles) == 0:
            raise GameOver("Board is full. Cannot spawn any tile.")
        if random_tile:
            #here we use logic that spawning 4 probability is 0.1 else spawn 2
            if random.random()<=0.1:
                self.board[random.choice(self.empty_tiles())] = 2
            else:
                self.board[random.choice(self.empty_tiles())] = 1

        else:
            pass
            #complete the code here

    def clear(self):
        self.board = [0] * 16
        

    

    def display(self):  
        def format_row(lst):
            s = ""
            for l in lst:
                s += " {:3d}".format(l)
            return s

        for row in range(4):
            idx = row * 4
            print(format_row(self.base10_board[idx : idx + 4]))

    @property
    def base10_board(self):  # this is the actual viewable board that we see
        return [2 ** v if v > 0 else 0 for v in self.board]

    def act(self, a):        #basically we wrote code to act as if swiping left, and used it for different use cases like up, down , right, by rotate function
        original = self.board
        if a == LEFT:
            r = self.merge_to_left()
        if a == RIGHT:
            r = self.rotate().rotate().merge_to_left()
            self.rotate().rotate()
        if a == UP:
            r = self.rotate().rotate().rotate().merge_to_left()
            self.rotate()
        if a == DOWN:
            r = self.rotate().merge_to_left()
            self.rotate().rotate().rotate()

        if original == self.board:
            raise IllegalAction("Action did not move any tile.")
        return r

    def rotate(self):
        "Rotate the board inplace 90 degress clockwise."
        size = 4
        b = []
        for i in range(size):
            b.extend(self.board[i::4][::-1])
        self.board = b
        return self

    def merge_to_left(self):
        "merge board to the left, returns the reward for merging tiles"
        "Raises IllegalAction exception if the action does not move any tile."
        r = []
        board_reward = 0
        for nrow in range(4):
            curr=self.board[nrow]
            reward,a=merge(curr)
            board_reward+=reward
            r.extend(a)
                
                
            #Complete the code here
        self.board = r
        return board_reward

    def copyboard(self):
        return copy(self.board)