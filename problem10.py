import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = 2 * 10 ** 6

import math
#nまでの素数のリスト
def eratosthenes(n): #必要な分だけ用意
    if n < 2: #1は素数ではない
        return []
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p: #limit=root(n)
            return prime + data #root(n)まで判定すれば、残りは全て素数であると言える
        prime.append(p)
        data = [e for e in data if e % p != 0] #エラトステネスのふるい

print(sum(eratosthenes(n)))