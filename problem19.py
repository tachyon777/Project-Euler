import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
thirty_one = [1,3,5,7,8,10,12]
count = 1 #1990.1.1が月曜日なので1から
ans = 0
month = 1
year = 1900
while True:
    if year >= 2001:
        print(ans)
        exit()
    if year > 1900:
        if count%7==0:
            ans += 1
    if month == 2:
        if year % 100 == 0:
            if year % 400 == 0:
                days = 29
            else:
                days = 28
        else:
            if year%4 == 0:
                days = 29
            else:
                days = 28
    elif month in thirty_one:
        days = 31
    else:
        days = 30
    count += days
    month = month+1 if month < 12 else 1
    if month == 1:
        year += 1