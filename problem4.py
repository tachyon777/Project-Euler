import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

def func(s):
    l = len(s)//2
    flag = 1
    for i in range(l):
        if s[i] != s[-1-i]:
            flag = 0
            break
        
    return flag

lst1 = []
for i in range(100,1000):
    for j in range(100,1000):
        s = str(i*j)
        if func(s):
            lst1.append(int(s))

print(max(lst1))