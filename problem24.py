import sys
import itertools
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = 10**6
lst1 = [i for i in range(10)]

res = list(itertools.permutations(lst1))[n-1]

print("".join(map(str,res)))