#!/bin/python3
import os

def compareTriplets(a, b):
    i=0
    alice_score=0
    bob_score=0
    while i<3:
        if a[i]>b[i]:
            alice_score+=1
        elif a[i]<b[i]:
            bob_score+=1
        i+=1
    return [alice_score,bob_score]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
