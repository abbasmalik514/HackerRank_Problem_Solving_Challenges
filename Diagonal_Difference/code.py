#!/bin/python3
import os

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    num_rows = len(arr)
    num_col = len(arr[0])
    ld_sum=0
    rd_sum=0
    for i in range(num_rows):
        ld_sum+=arr[i][i]
        rd_sum+=arr[i][num_rows-1-i]
    return abs(ld_sum - rd_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
