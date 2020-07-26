#!/bin/python3
import os

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    count=0
    cur_height = 0
    for i in ar:
        if i==cur_height:
            count+=1
        elif i>cur_height:
            cur_height=i
            count=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
