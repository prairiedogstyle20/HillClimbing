#! /usr/bin/python

import random
import math
#
# Assignment 2 for CS480
#

class Hillclimb:
    def __init__(self):
        self.x_value = random.randrange(-10001,10001)
        self.y_value = random.randrange(-10001,10001)
        self.max_value = 10000
        self.min_value = -10000
    #
    # Generate the new value of X
    #
    def gen_x(self,curr_x):
        new_x = (random.random() - 0.5)*0.1 + curr_x
        return new_x
#
# Generate the new value of Y
#
    def gen_y(self,curr_y):
        new_y = (random.random() - 0.5)*0.1 + curr_y
        return new_y
#
#
#
    def gen_egg_value(self, x, y):
        y47 = y + 47
        egg_v = -(y47)*math.sin(math.sqrt(abs((x/2)+(y47)))) - (x*(math.sin(abs(x-y47))))
        return egg_v
#
#
#
def main():

    f = open('HC_output.txt','w')

    for num in range(0,101):
        print(num)
        my_climber = Hillclimb()
        curr_egg_v = my_climber.gen_egg_value(my_climber.x_value, my_climber.y_value)
        f.write(f"start position is x:{my_climber.x_value}, y:{my_climber.y_value}" + '\r\n')
        f.write(f"start egg value {curr_egg_v}" + '\r\n')
        num_last_min = 0
        while num_last_min < 101:
            calc_x = my_climber.gen_x(my_climber.x_value)
            calc_y = my_climber.gen_y(my_climber.y_value)
            new_egg_v = my_climber.gen_egg_value(calc_x,calc_y)
            if new_egg_v < curr_egg_v:
                curr_egg_v = new_egg_v
                my_climber.x_value = calc_x
                my_climber.y_value = calc_y
                #f.write(f'New low is x:{calc_x}, y:{calc_y}' + '\r\n')
                num_last_min = 0
            else:
                num_last_min = num_last_min + 1

        f.write(f'EXIT position is x:{my_climber.x_value}, y:{my_climber.y_value}' + '\r\n')
        f.write(f"{curr_egg_v}" + '\r\n' + '\r\n')
    f.close()
    return

main()
