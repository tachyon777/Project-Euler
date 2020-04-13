import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = 1000
for i in range(1,n-1):
    for j in range(1,n-1):
        k = n-i-j
        if k >= 1:
            if i**2 + j**2 == k**2:
                print(i*j*k)
                exit()