#! /usr/bin/python

import random
import math
import copy
from colorama import *

class Queen():
    def __init__(self, xpos, ypos):
        self.pos_x = xpos
        self.pos_y = ypos

    def set_x(self,new_x):
        self.pos_x = new_x

    def set_y(self,new_y):
        self.pos_y = new_y

class Board:
    def __init__(self):
        self.size = 0
        self.num_queen = self.size
        self.queens_list = []
        self.fscore = 0

    # set the board size
    def set_size(self, num):
        self.size = num

    def check_pos_open(self, curr_x, curr_y):
        for i in self.queens_list:
            if i.pos_x == curr_x and i.pos_y == curr_y:
                return False
            else:
                continue
        return True

    def place_queens(self):
        for i in range (self.size):
            queen_x = random.randrange(0,self.size)
            queen_y = i
            can_add = self.check_pos_open(queen_x,queen_y)
            while can_add == False:
                queen_x = random.randrange(0,self.size)
                queen_y = i
                can_add = self.check_pos_open(queen_x,queen_y)

            self.queens_list.append(Queen(queen_x,queen_y))

class Solver:
    def __init__(self):
        self.population = 1
        self.board_list = []
        #self.board = Board()

    def populate_board_list(self,b_size):
        for i in range(self.population):
            self.board_list.append(Board())
            self.board_list[i].set_size(b_size)
            self.board_list[i].place_queens()

    def hill_climb_queen(self):
        done = False
        for b in self.board_list:
            #curr_queen = random.choice(b.queens_list)
            while done == False:
                for queen in b.queens_list:
                    if done == True:
                        break
                    for i in range(b.size):
                        if i == queen.pos_y:
                            continue
                        else:
                            copy_found = False
                            test_copy = copy.deepcopy(b)
                            while copy_found == False:
                                for testq in test_copy.queens_list:
                                    if queen.pos_x == testq.pos_x and queen.pos_y == testq.pos_y:
                                        testq.set_y(i)
                                        copy_found = True
                                    else:
                                        continue
                            test_copy.gen_fitness_score()
                            if test_copy.fscore == 0:
                                done = True
                                break
                            elif test_copy.fscore < b.fscore:
                                b.board_list[0] = test_copy


    def genetic_selection(self):
        pass

    def gen_children(self):
        pass

    def apply_mutation(self):
        pass

    def gen_fitness_score(self):
        for b in self.board_list:
            for q in b.queens_list:
                for p in b.queens_list:
                    if q.pos_x == p.pos_x and q.pos_y == p.pos_y:
                        continue
                    elif q.pos_x == p.pos_x:
                        b.fscore = b.fscore + 1
                    elif q.pos_y == p.pos_y:
                        b.fscore = b.fscore + 1
                    else:
                        continue
                self.check_posx_posy(q.pos_x, q.pos_y)
                self.check_posx_negy(q.pos_x, q.pos_y)
                self.check_negx_posy(q.pos_x, q.pos_y)
                self.check_negx_negy(q.pos_x, q.pos_y)
        if b.fscore != 0:
            b.fscore = b.fscore/2

    def check_posx_posy(self, curr_x, curr_y):
        for b in self.board_list:
            while curr_x < b.size and curr_y < b.size:
                curr_x = curr_x + 1
                curr_y = curr_y + 1
                for i in b.queens_list:
                    if i.pos_x == curr_x and i.pos_y == curr_y:
                        b.fscore = b.fscore + 1

    def check_posx_negy(self, curr_x, curr_y):
        for b in self.board_list:
            while curr_x < b.size and curr_y >= 0:
                curr_x = curr_x + 1
                curr_y = curr_y - 1
                for i in b.queens_list:
                    if i.pos_x == curr_x and i.pos_y == curr_y:
                        b.fscore = b.fscore + 1

    def check_negx_posy(self, curr_x, curr_y):
        for b in self.board_list:
            while curr_x >= 0 and curr_y < b.size:
                curr_x = curr_x - 1
                curr_y = curr_y + 1
                for i in b.queens_list:
                    if i.pos_x == curr_x and i.pos_y == curr_y:
                        b.fscore = b.fscore + 1

    def check_negx_negy(self, curr_x, curr_y):
        for b in self.board_list:
            while curr_x >= 0 and curr_y >= 0:
                curr_x = curr_x - 1
                curr_y = curr_y - 1
                for i in b.queens_list:
                    if i.pos_x == curr_x and i.pos_y == curr_y:
                        b.fscore = b.fscore + 1

    def display_board(self):
        for b in self.board_list:
            for i in range(b.size):
                for j in range(b.size):
                    if b.check_pos_open(i,j) == False and j == b.size-1:
                        print( Fore.RED + 'Q')
                    elif b.check_pos_open(i,j) == False and j != b.size-1:
                        print( Fore.RED + 'Q', end =" ")
                    elif b.check_pos_open(i,j) == True and j == b.size-1:
                        print( Fore.BLUE + 'X')
                    elif b.check_pos_open(i,j) == True and j != b.size-1:
                        print(Fore.BLUE + 'X', end =" ")
                    elif i == b.size-1 and j == b.size-1:
                        continue
            print(f"Board fitness score: {b.fscore}")

def main():
    mysolver = Solver()
    mysolver.populate_board_list(8)
    mysolver.gen_fitness_score()
    #mysolver.board.set_size(8)
    #mysolver.board.place_queens()
    #mysolver.gen_fitness_score()
    mysolver.display_board()
    mysolver.hill_climb_queen()
    mysolver.display_board()

main()
