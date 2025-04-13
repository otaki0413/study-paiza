# 旅程日数
N = int(input())
times = []
for _ in range(N):
    s, f, t = map(int, input().split())
    sum = s + f + (24 - t)
    times.append(sum)

print(min(times))
print(max(times))


# # 関数バージョン
# def calc_daily_hour(departure_time, flight_time, arrival_time):
#     return departure_time + flight_time + (24 - arrival_time)


# N = int(input())
# daily_hours = []

# # N日分の時間を計算
# for _ in range(N):
#     departure_time, flight_time, arrival_time = map(int, input().split())
#     daily_hour = calc_daily_hour(departure_time, flight_time, arrival_time)
#     daily_hours.append(daily_hour)

# print(min(daily_hours))
# print(max(daily_hours))
