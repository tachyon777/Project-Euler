import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = 4 * 10 ** 6

dp = [1,2]
ans = 2
while True:
    res = dp[-2] + dp[-1]
    if res > n:
        break
    else:
        if res%2 == 0:
            ans += res
        dp.append(res)
print(ans)