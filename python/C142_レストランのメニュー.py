S = input()  # 食べたい料理名（1つ）
N = int(input())  # メニューの単語数
menu = input().split()  # メニュー名

result = "No"
for i in range(N):
    if menu[i] == S:
        result = "Yes"
        break

print(result)


# 要素を直接イテレートするパターン
# S = input()
# N = int(input())
# menu = input().split()

# result = "No"
# for menu_item in menu:
#     if menu_item == S:
#         result = "Yes"
#         break

# print(result)
