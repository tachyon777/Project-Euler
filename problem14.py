import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
#二項係数(modなし) O(k)
def large_conbination(n,k): #no mod. return nCk.
    res1 = 1
    for i in range(n,n-k,-1):
        res1*=i
    res2 = 1
    for i in range(1,k+1):
        res2*= i
    return res1//res2

print(large_conbination(40,20))