import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = 1000
ans = 0
for i in range(1,n):
    if i%3==0 or i%5==0:
            ans += i
print(ans)