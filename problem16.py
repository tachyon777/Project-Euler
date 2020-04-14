import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

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

n = 1000

s = str(pow(2,n))

ans = 0
for i in s:
    ans += int(i)
print(ans)
