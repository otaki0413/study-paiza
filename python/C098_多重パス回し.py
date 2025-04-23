# 人の人数
N = int(input())
users = {}
for i in range(N):
    users[i + 1] = int(input())

# パスの回数
M = int(input())
for _ in range(M):
    passer, receiver, count = map(int, input().split())
    if users[passer] < count:
        users[receiver] += users[passer]
        users[passer] = 0
    else:
        users[receiver] += count
        users[passer] -= count

for value in users.values():
    print(value)


## 別回答
## 関数として切り出す
def process_ball_passes(users, passes):
    for passer, receiver, count in passes:
        if users[passer] < count:
            users[receiver] += users[passer]
            users[passer] = 0
        else:
            users[receiver] += count
            users[passer] -= count


N = int(input())
users = {}
for i in range(N):
    users[i + 1] = int(input())

M = int(input())
passes = [tuple(map(int, input().split())) for _ in range(M)]
process_ball_passes(users, passes)

for value in users.values():
    print(value)
