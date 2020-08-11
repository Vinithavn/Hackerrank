#importing libraries

import math
import os
import random
import re
import sys

def biggerIsGreater(w):
    string=""
    flag=False
    if len(w)>1:
        #whenever the current letter of the string is greater than the previous letter then we need to edit string from that position
        for i in range(len(w)-1,0,-1):
            if w[i]>w[i-1]:
                flag=True   #if such a case occur, the falg=true else it will remain as False
                break
            
        sort=sorted(w[i-1:]) # the list of letters starting from the position that needs to be edited
    
        for k in sort:
            if k >w[i-1]: # find out the next higher letter than the letter in current position 
            
                break
    
        string=w[:i-1]+k # add the next higher letter after the current position in the string
   
        sort.remove(k)
    
    
        for ele in sort:
            string+=ele   # add the remaining letters to be added to the string
        
    

    if flag==True:
        
        return string
    else:
        return "no answer"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
