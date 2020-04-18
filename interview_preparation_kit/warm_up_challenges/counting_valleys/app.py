#!/bin/python3

import math
import os


# Complete the countingValleys function below.
def countingValleys(n, s):
    counter = 0
    if n >= 2 and n <= math.pow(10, 6):  # Constraint 1
        altitude = 0
        for step in s:
            if step == 'U':  # Constraint 2
                if altitude == -1:
                    counter += 1
                altitude += 1
            elif step == 'D':  # Constraint 2
                altitude -= 1
            else:
                err_msg = '"{}" is not a valid step'.format(step)
                raise ValueError(err_msg)
    else:
        err_msg = '"{}" is not a valid number of steps.'.format(n)
        raise ValueError(err_msg)
    return counter


if __name__ == '__main__':
    n = 9
    s = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']
    print(countingValleys(n, s))
