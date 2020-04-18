import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = 100

lst1 = []
def pow(n,p): #繰り返し二乗法(nのp乗)
    res = 1
    while p > 0:
        if p % 2 == 0:
            n = n ** 2
            p //= 2
        else:
            res = res * n
            p -= 1
    return res
for i in range(2,n+1):
    for j in range(2,n+1):
        lst1.append(pow(i,j))

print(len(set(lst1)))