import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

dp = [1,1]

while True:
    if len(str(dp[-1]+dp[-2])) == 1000:
        print(len(dp)+1)
        exit()
    dp.append(dp[-1]+dp[-2])