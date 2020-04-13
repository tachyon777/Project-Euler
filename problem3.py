import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

"""素因数分解"""
def factrize(n):
    b = 2
    fct = []
    while b*b <= n:
        while n % b == 0:
            n //= b
            #もし素因数を重複させたくないならここを加えてfct.append(b)を消す
            """
            if not b in fct:
                fct.append(b)
            """
            fct.append(b)
        b = b+1
    if n > 1:
        fct.append(n)
    return fct #リストが帰る

n = 600851475143

print(max(factrize(n)))