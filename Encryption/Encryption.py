#importing libraries

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    #finding the number of colummns and rows
    if int(math.sqrt(len(s)))==math.sqrt(len(s)):
        row=int(math.sqrt(len(s)))
        col=int(math.sqrt(len(s)))
    else:
        row=int(math.sqrt(len(s)))
        col=row+1
      
    string=""
    print(row,col)
    for i in range(col):
        s1=""
        while(i<len(s)):
            s1+=s[i] 
            
            i+=col    #add the letters to string s1 which are in a seperated by the number of columns. This will give each word
        string+=s1+" "  
    print(string) 
    return string
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
