import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = 1000

"""素数判定"""
def factrize(n):
    b = 2
    while b*b <= n:
        if n % b == 0:
            return False
        b = b+1
    return True

def func(x,a,b):
    return x**2 + a*x + b

ans_a = None
ans_b = None
count = 0
for a in range(-n+1,n):
    if a%100 == 0:print("progress:",a)
    for b in range(-n+1,n):
        i = 0
        while 1:
            res = func(i,a,b)
            if res < 0:
                break
            if factrize(res):
                pass
            else:
                if i > count:
                    ans_a = a
                    ans_b = b
                    count = i
                break

            i += 1

print(ans_a*ans_b)