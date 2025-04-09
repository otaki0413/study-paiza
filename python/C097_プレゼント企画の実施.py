N, X, Y = map(int, input().split())

for i in range(N):
    num = i + 1
    if (num % X == 0) and (num % Y == 0):
        print("AB")
    elif num % X == 0:
        print("A")
    elif num % Y == 0:
        print("B")
    else:
        print("N")
