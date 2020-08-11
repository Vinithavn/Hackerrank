#importing bunch of libraries

import math
import os
import random
import re
import sys


def queensAttack(n, k, r_q, c_q, obstacles):
  #maximum farthest possible location of obstacles in 8 different directions from the queen
  
    right=(r_q,n+1) #right side of the queen
    left=(r_q,0)    #left side of the queen
    top=(n+1,c_q)   #top side of the queen
    down=(0,c_q)    #bottom side of the queen
    right_c=(n+1,n+1) #right up corner
    left_c=(n+1,0)    #left up corner
    right_c_down=(0,n+1)  #right down corner
    left_c_down=(0,0)     #left down corner

    for each in obstacles:
        ox=each[0]
        oy=each[1]
        # finding the nearesrt obstacle in the above eight directions from the queen
        if ox==r_q:
            if oy<=right[1] and oy>c_q:
                right=(ox,oy)
            elif oy>=left[1] and oy<c_q:
                left=(ox,oy)
        
        elif oy==c_q:
            if ox<=top[0] and ox>r_q:
                top=(ox,oy)
            elif ox>=down[0] and ox<r_q:
                down=(ox,oy)
            
        elif (ox-oy)== (r_q-c_q):
            if ox>r_q and ox<=right_c[0] and oy>c_q and oy<=right_c[1]:
                right_c=(ox,oy)
            elif ox<r_q and ox>=left_c_down[0] and oy<c_q and oy>=left_c_down[1]:
                left_c_down=(ox,oy)
        elif (ox+oy)==(r_q+c_q):
            if ox>r_q and ox<=left_c[0] and oy<c_q and oy>=left_c[1]:
                left_c=(ox,oy)
            elif ox<r_q and ox>=right_c_down[0] and oy>c_q and oy<=right_c_down[1]:
                right_c_down=(ox,oy)
    
    #after getting all the nearest obstacles, return the number of attacks for the queen
    return (right[1]-c_q-1)+(c_q-left[1]-1)+min(right_c[0]-r_q-1,right_c[1]-c_q-1)+min(r_q-right_c_down[0]-1,right_c_down[1]-c_q-1)+min(left_c[0]-r_q-1,c_q-left_c[1]-1)+min(r_q-left_c_down[0]-1,c_q-left_c_down[1]-1)+(top[0]-r_q-1)+(r_q-down[0]-1)





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
