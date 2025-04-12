# 定数
CORRECT = "y"
INCORRECT = "n"

N = int(input())

retry_numbers = []
for i in range(N):
    A, B = input().split()
    todo_number = i + 1
    if A == INCORRECT or B == INCORRECT:
        retry_numbers.append(todo_number)

print(len(retry_numbers))
for number in retry_numbers:
    print(number)
