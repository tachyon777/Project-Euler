import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = 46000
kijun = ord("A")

file_ = open("p022.txt").read()
lst1 = file_.split(",")
for i in range(len(lst1)):
    lst1[i] = lst1[i].replace('"','')
lst1.sort()
ans = 0
for i,j in enumerate(lst1,1):
    res = 0
    for k in j:
        res += ord(k)-kijun+1
    ans += i*res
print(ans)