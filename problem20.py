import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = 100

def factrial_memo(n=10**5):
    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i))
    return fact
fact = factrial_memo(n)

s = str(fact[-1])
ans = 0
for i in s:
    ans += int(i)
print(ans)