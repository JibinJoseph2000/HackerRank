import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    p=0
    q=0
    ar=[]
    for i in range(0,3):
        if((a[i]>0 and a[i]<101) and (b[i]>0 and b[i]<101)):
            if(a[i]>b[i]):
                p=p+1
            if(a[i]<b[i]):
                q=q+1
    ar.append(p)
    ar.append(q)
    return ar
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))
    result = []
    result =compareTriplets(a,b)
    print(result[0],result[1])
    fptr.write(' '.join(map(str, result)))    
    fptr.write('\n') 
