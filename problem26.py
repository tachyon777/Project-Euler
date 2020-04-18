import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = 1000

#1/xの循環小数の長さを求める
def decimal(x):
    count = 0
    rec_lst = []
    rec = 10
    while True:
        rec %= x

        if rec in rec_lst: #過去に出現した余りなら循環終了
            break

        rec_lst.append(rec)
        count += 1
        rec *= 10
    
    cyc_len = count - rec_lst.index(rec) + 1
    return cyc_len

ans = 0
for i in range(1,n):
    ans = max(ans,decimal(i))

print(ans)