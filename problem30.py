import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = 10**6
ans = 0
for i in range(10,n+1):
    if i%(10**4)==0:
        print("progress:",i,"/",n)
    res = str(i)
    res2 = 0
    for j in res:
        res2 += pow(int(j),5)
    if res2==i:
        ans += i

print(ans)