import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = 1000

numbers = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 
           6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 
           11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 
           16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 
           30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 
           80:"eighty", 90:"ninety", 1000:"one thousand"}

def counter(s):
    return len(s.replace(" ","").replace("-",""))

ans = 0

for i in range(1,n+1):
    if i in numbers:
        ans += counter(numbers[i])
    elif i < 100:
        a = i % 10
        b = (i // 10) * 10
        ans += counter(numbers[b] + numbers[a])
    else:
        a = i % 100
        b = i // 100
        if a == 0:
            ans += counter(numbers[b] + "hundred")
        else:
            ans += counter(numbers[b] + "hundred and")
            if a in numbers:
                ans += counter(numbers[a])
            else:
                c = a % 10
                d = (a // 10) * 10
                ans += counter(numbers[c] + numbers[d])


print(ans)