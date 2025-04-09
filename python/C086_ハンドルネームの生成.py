lower_boin_list = ["a", "e", "i", "o", "u"]
upper_boin_list = ["A", "E", "I", "O", "U"]

S = input()
result = []

for char in S:
    if char not in lower_boin_list and char not in upper_boin_list:
        result.append(char)

print("".join(result))

# もっとシンプルにかくならこうする
# S = input()
# result = [c for c in S if c not in "aeiouAEIOU"]
# print("".join(result))
