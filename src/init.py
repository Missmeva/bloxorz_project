import random 

class Position():

    def __init__(self, position, step_no = 0):
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.closed_list = []
        self.step_no = step_no
        self.position = position


    def insert(self, current_position, direction, step_no=0):
        '''Inserts a move into position tree of bloxorz game
                current_position: a value from {0, 1}, 0 - standing, 1 - laying
                direction: a value from {0, 1, 2, 3} - left, right, up, down
                step_no: a number identifying current step per each path choice'''

        if direction == 0:
            if self.left is None:
                self.left = Position(current_position, step_no)
                self.left.closed_list.append(self.position)
            elif step_no>self.step_no:
                self.left.insert(current_position, direction, step_no)
        elif direction == 1:
            if self.right is None:
                self.right = Position(current_position, step_no)
                self.right.closed_list.append(self.position)
            elif step_no>self.step_no:
                self.right.insert(current_position, direction, step_no)
        elif direction == 2:
            if self.up is None:
                self.up = Position(current_position, step_no)
                self.up.closed_list.append(self.position)
            elif step_no>self.step_no:
                self.up.insert(current_position, direction, step_no)
        elif direction == 3:
            if self.down is None:
                self.down = Position(current_position, step_no)
                self.down.closed_list.append(self.position)
            elif step_no>self.step_no:
                self.down.insert(current_position, direction, step_no)
        return self

    def print_moves(self):
        '''Print combination of paths found'''
        print(self.position, ", step ", self.step_no)
        print("closed list: ", self.closed_list)
       
        if self.left:
            print("LEFT: ")
            self.left.print_moves()
        if self.right:
            print("RIGHT: ")
            self.right.print_moves()
        if self.up:
            print("UP: ")
            self.up.print_moves()
        if self.down:
            print("DOWN: ")
            self.down.print_moves()


if __name__ == '__main__':
    # generate a sample board in the form of a binary map
    board = [[1,1,1,0,0,0,0,0],
            [1,1,1,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,1,1,0,0,1,1,1],
            [1,1,1,0,0,1,1,1],
            [1,1,1,0,0,1,1,1]]

    start_pos = [0,3]
    end_pos = [7,5]

    # initiate a bloxorz block
    moves_tree = Position(start_pos)

    # make actual move
    move_a_1 = moves_tree.insert([[1,3], [2,3]], 1, 1) #right
    move_b_1 = moves_tree.insert([[0,1], [0,2]], 2, 1) #right
    move_a_2 = move_b_1.insert([[1,2], [2,2]], 2, 2) #up
    moves_tree.print_moves()