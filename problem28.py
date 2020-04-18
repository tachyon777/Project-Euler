import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = 1001*1001

now = 0
space = 0
cycle = 3
ans = 0
while 1:
    if now >= n:
        break
    ans += now+1
    cycle += 1
    if cycle%4==0:
        space += 2
    now += space

print(ans)