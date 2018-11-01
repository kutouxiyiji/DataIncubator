# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:29:55 2017

@author: kutouxiyiji
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 10:48:18 2017

@author: kutouxiyiji
"""

import numpy as np
import random
import math

#next move
def Move(i,j):
    Knight_move = np.matrix([[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]])
    next_x = {}
    next_y = {}
    k = 0
    p = 0 #number of possible movements
    while k <8: #all possible moves
        x = i + Knight_move[k,0]
        y = j + Knight_move[k,1]
        if x>=0 and x<=3 and y>=0 and y<=3: #size of chess board
            next_x[p] = x
            next_y[p] = y
            p+=1
        k+=1
    if p > 0:
        decision = random.randint(0,p-1)
        return (next_x[decision],next_y[decision])
    else:
        print("Error! no possible movement!")

if __name__ == "__main__":
    repeat = 50000
#    Modulo = 13 # modulo
    repeat_number = repeat
    statistical_sum = 0
    SUM={}
    count_43 = 0
    count_7 = 0
    while repeat >0:
        T =512  #total moves
        Knight_value = np.matrix([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
        (i,j) = (0,0)
        SUM[repeat] = 0
        while T>0:
            (i,j) = Move(i,j)
            SUM[repeat] += Knight_value[i,j]
            T-=1
        if SUM[repeat]%43 ==0:
            count_43 +=1
            if SUM[repeat]%7 ==0:
                count_7 +=1
        repeat -=1
    print count_7
    print count_43
    print('result is ' + format(float(count_7)/float(count_43),'.16f'))

#    print mean