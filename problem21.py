import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = 10000


def d(x):
    res = 0
    for i in range(1,x//2+1):
        if x%i==0:
            res += i
    return res
ans = []
for i in range(1,n+1):
    res = d(i)
    if res != i and d(res) == i:
        ans.append(res)

print(sum(ans))