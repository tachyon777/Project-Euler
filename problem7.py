import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
#n番目までの素数のリスト
def generate_primes(n):
  primes = [2]
  i = 3
  count = 1
  while count < n:
    for p in primes:
      if i % p == 0:
        break
    else:
      primes.append(i)
      count += 1
    i += 2
  return primes

n = 10001

#n番目までの素数のリスト
primes = generate_primes(n)

print(primes[-1])