import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
ans = 0
for i in range(100):
    ans += int(readline())
print(str(ans)[:10])