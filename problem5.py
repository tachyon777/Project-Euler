import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return (a//gcd(a,b)*b)

ans = 1
for i in range(1,20):
    ans = lcm(ans,i)

print(ans)