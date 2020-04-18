import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = 28123 #これ以上の数字は必ず2つの豊富数の和で表せる

abundant = [] #豊富数

"""約数の列挙"""
def factrize(n):
    b = 1
    res = 0
    while n//2 >= b:
        if n%b==0:
            res += b
        b += 1
    
    return res

#その値が含まれているかどうかを調べる2分探索
def func(mid,x,lst1): #ここが関数部分
    #-1:ngをmidに、0:丁度その値が含まれている。1:okをmidに
    if lst1[mid] == x:
        return 0
    elif lst1[mid] < x:
        return -1
    else: #lst1[mid] > x
        return 1

def binary_search(x,lst1): #x:xが入っているかどうかを２分探索
    ok = len(lst1) #リストの長さだけ
    ng = -1 #(リストに対しては)固定
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        res = func(mid,x,lst1)
        if res == -1:
            ng = mid
        elif res == 1:
            ok = mid
        else: #==0:含まれる
            return True

    return False

for i in range(1,n+1):
    if i%1000==0:
        print("processing:",i,"/",n)
    if factrize(i) > i: #完全数を含まない
        abundant.append(i)
print(len(abundant)) #6965あるので全列挙だと莫大な時間がかかる
#片方決め打って、もう片方が存在するかどうかの二分探索が良さそう。
now = 0
ans = 0
for i in range(1,n+1):
    flag = 0 #2つの豊富数の和で表せるなら1
    for j in abundant:
        k = i-j
        if k <= 0:
            break
        if binary_search(k,abundant):
            flag = 1
            break

    if not flag:
        ans += i

print(ans)