#!/bin/python3


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max_sum_4=0
    min_sum_4=11111111111111
    array_size = len(arr)
    for i in range(array_size):
        sum_4 = 0
        for j in range(array_size):
            if j==i:
                continue
            sum_4+=arr[j]

        if sum_4 > max_sum_4:
            max_sum_4 = sum_4
        if sum_4 < min_sum_4:
            min_sum_4 = sum_4
    
    print(str(min_sum_4)+' '+str(max_sum_4))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
