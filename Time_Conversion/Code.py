#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    txt=s.split(':')
    if txt[2][2:] == 'AM':
        if txt[0] == '12':
            txt[0] = '00'
    else:
        if txt[0] != '12':
            txt[0]=str(int(txt[0])+12)
    return txt[0]+':'+txt[1]+':'+txt[2][0:2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
