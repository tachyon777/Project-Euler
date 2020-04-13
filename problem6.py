import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = 100

res1 = 0
res2 = 0

for i in range(1,n+1):
    res1+=i
    res2+=i**2

print(res1**2-res2)