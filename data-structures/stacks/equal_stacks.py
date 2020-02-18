# solution to hackerrank problem
# https://www.hackerrank.com/challenges/equal-stacks/problem

import os
import sys
from functools import reduce


def equalStacks(h1, h2, h3):

    # if one of the lists has 0 elements return 0
    if len(h1) == 0 or len(h2) == 0 or len(h3) == 0:
        return 0 

    # if all of the lists are equal height
    elif sum(h1) == sum(h2) and sum(h1) == sum(h3):
        return sum(h1)

    else:

        # function to get the sum at each block
        def sum_list(l):
            l = l[::-1]
            sum_list = [0]

            for i in l:
                sum = i + sum_list[-1:][0]
                sum_list.append(sum)
            
            return sum_list
        
        h1_sum_list = sum_list(h1)
        print(h1_sum_list, 'h1 sum list')

        h2_sum_list = sum_list(h2)
        print(h1_sum_list, 'h2 sum list')

        h3_sum_list = sum_list(h3)
        print(h1_sum_list, 'h3 sum list')
        
        # list of sum lists
        h_list = [h1_sum_list, h2_sum_list, h3_sum_list]

        # find common sums between the lists
        common_heights = list(reduce(lambda i, j: i & j, (set(x) for x in h_list)))
        print(common_heights)

        # return the maximum common height
        return max(common_heights)
