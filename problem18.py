import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

"""
貪欲で解けるが、n=100(今回は15)となった場合を考えてdpを組む。
(problem67が同問のn=100)
"""

n = 15
lst1 = []
for i in range(n):
    res = list(map(int,readline().split()))
    lst1.append(res)

dp = [[0]*(i+1) for i in range(n)] #dp[i][j]:i段目の左からj番目にいる時、(そこを含め)そこから得られる利益の最大値
dp[0][0] = lst1[0][0]

for i in range(1,n):
    for j in range(i+1):
        #j=0からはdp[i-1][0]しか参照できず、j=iからはdp[i-1][j-1]しか参照できない。
        if j==0:
            dp[i][j] = dp[i-1][0] + lst1[i][j]
        elif j==i:
            dp[i][j] = dp[i-1][j-1] + lst1[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + lst1[i][j]

print(max(dp[-1]))

