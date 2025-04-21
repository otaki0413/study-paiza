total_hour = 0
total_min = 0

N = int(input())
for _ in range(N):
    s, e = input().split()
    s_hour, s_min = map(int, s.split(":"))
    e_hour, e_min = map(int, e.split(":"))

    # 時分の差分比較
    if e_min - s_min >= 0:
        diff_hour = e_hour - s_hour
        diff_min = abs(e_min - s_min)
    else:
        diff_hour = e_hour - s_hour - 1
        diff_min = 60 - abs(e_min - s_min)

    total_hour += diff_hour
    total_min += diff_min


# 合計分数を60で割ったときの商と余りを求める
q, r = divmod(total_min, 60)
total_hour += q
total_min = r

print(f"{total_hour} {total_min}")


# ---------------------------------------------------
# 別解（分換算して差分計算）
N = int(input())
total_minutes = 0

for _ in range(N):
    s, e = input().split()
    s_hour, s_min = map(int, s.split(":"))
    e_hour, e_min = map(int, e.split(":"))

    start = s_hour * 60 + s_min
    end = e_hour * 60 + e_min
    diff = end - start

    total_minutes += diff

H = total_minutes // 60
M = total_minutes % 60

print(H, M)
