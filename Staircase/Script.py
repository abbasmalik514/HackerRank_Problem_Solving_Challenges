def staircase(n):
    i = n-1
    while(i>=0):
        j=i-1
        while(j>=0):
            print(' ',end='')
            j-=1
        k=n-i-1
        while(k>=0):
            print('#',end='')
            k-=1
        i-=1
        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)
