#importing bunch of libraries

import math
import os
import random
import re
import sys


def organizingContainers(containers):
        
        #two dictionaries are created to count (a) the number of each type of ball (b) the number of balls each container can carry
        ball_count=dict()
        sum_1=dict()
        for each in range(len(container[0])):
            
            for i in range(len(container)):
                
                sum_1["container"+str(i+1)]=sum(container[i])
            
                if str(each+1) in ball_count:
                    ball_count[str(each+1)]+=container[i][each]
                else:
                    ball_count[str(each+1)]=container[i][each]
        
        # when we compare the list of values of both the dictionaries, if both lists are matched, then the balls can be grouped into each containers, otherwise not.
        q=list(sum_1.values())
        r=list(ball_count.values())  
          
        if sorted(q)==sorted(r):
            return "Possible"
        else:
            return "Impossible"           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
