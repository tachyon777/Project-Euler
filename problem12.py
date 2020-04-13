import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

"""約数の個数"""
#参考：青チャp280
#注意：1も約数としてカウントされる
def factrize(n):
    b = 2
    fct = []
    while b*b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b+1
    if n > 1:
        fct.append(n)
    if len(fct) == 1: #素数だった場合
        return 2 #1と、その数の2通り
    
    divisor = dict()
    for i in fct:
        if not i in divisor:
            divisor[i] = 1
        else:
            divisor[i] += 1
    ans = 1
    for i in divisor.values():
        ans *= (i+1)
    return ans

i = 1
res = 1
while True:
	if factrize(res) > 500:
		print(res)
		break
	i += 1
	res += i