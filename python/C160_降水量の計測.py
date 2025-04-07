import math

N = int(input())
L = map(int, input().split())

avg = math.ceil(sum(L) / N)
print(avg)
