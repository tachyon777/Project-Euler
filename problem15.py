import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = 10**6

def func(x):
    count = 0
    while True:
        if x == 1:
            return count
        if x%2==0:
            x //= 2
        else:
            x = 3*x + 1
        count += 1

ans = 0
mx = 0
for i in range(1,n+1):
    res = func(i)
    if mx < res:
        ans = i
        mx = res

print(ans)