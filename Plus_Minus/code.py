#!/bin/python3

# Complete the plusMinus function below.
def plusMinus(arr):
    plus_count = negative_count = zero_count=0
    for i in arr:
        if i>0:
            plus_count+=1
        elif i<0:
            negative_count+=1
        else:
            zero_count+=1
    total_size = len(arr)
    print("{:.6f}".format(float(plus_count/total_size)))
    print("{:.6f}".format(float(negative_count/total_size)))
    print("{:.6f}".format(float(zero_count/total_size)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
