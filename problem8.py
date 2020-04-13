import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

s = ""

for i in range(20):
    s += readline().rstrip().decode('utf-8')

i = 0
ans = 0
while 1:
    if i+13 >= len(s):
        print(ans)
        exit()
    
    if "0" not in s[i:i+13]:
        res = 1
        for j in range(13):
            res *= int(s[i+j])
        ans = max(res,ans)



    i += 1