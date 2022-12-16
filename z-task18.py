#  https://www.codewars.com/kata/540afbe2dc9f615d5e000425
#  Rules^

import numpy as np


class Sudoku(object):

    # Check if its n x n board (if it's valid)

    def check_n_x_n(data):
        length = len(data)
        for i in range(length):
            if len(data[i]) != length:
                return False

    # Check small sudoku squares (if sudoku is 9x9 then 3x3 will have numbers from 1 to 9 no duplicates)

    def small_arrays(data):
        length = len(data[0])

        data = np.array(data)
        small_squares = np.split(data, (int(length ** (1 / 2))), axis=1)

        small_squares = np.array(small_squares)

        small_squares = [item for sublist in small_squares for item in sublist]

        check_small = []
        for i in range(length):
            for j in range(int(length ** (1 / 2))):
                small_square_one_of_them = small_squares[(i * (int(length ** (1 / 2))) + j)]
                check_small.append(small_square_one_of_them)

            check_small = np.array(check_small)

            check_small = check_small.tolist()

            check_small = [item for sublist in check_small for item in sublist]

            # Check for duplicates

            if len(check_small) != len(set(check_small)):
                return False
            else:
                check_small = []

    # Check horizontally

    def check_hor(data):
        data = [d for d in data]

        for i in data:

            if len(i) != len(set(i)):
                return False

    # Check vertically

    def check_ver(data):
        data = np.rot90(data)

        for i in data:

            if len(i) != len(set(i)):
                return False

    def __init__(self, data):
        self.data = data


    # Edge cases

    def is_valid(self):
        if len(self.data) == 1 and type(self.data[0][0]) == bool:
            return False
        elif len(self.data) == 1 and self.data[0][0] == 1:
            return True

        elif len(self.data) == 1 and self.data[0][0] != 1:
            return False

        # Check output from every function

        nxn_valid = Sudoku.check_n_x_n(self.data)
        if nxn_valid == False:
            return False
        small_arrays = Sudoku.small_arrays(self.data)
        horizontally = Sudoku.check_hor(self.data)
        vertically = Sudoku.check_ver(self.data)
        if small_arrays != False and horizontally != False and vertically != False:
            return True
        else:
            return False
        
        
        
