N = int(input())

is_invalid = True
prev_back_text: str = ""
new_front_text: str = ""

for i in range(N):
    text = input()
    # 初回ループ時は末尾文字の更新
    if i == 0:
        prev_back_text = text[-1]
        continue

    # 前回の末尾の文字と今回の先頭文字を比較
    if prev_back_text != text[0]:
        new_front_text = text[0]
        is_invalid = False
        break

    # 末尾の文字更新
    prev_back_text = text[-1]

# しりとりが成り立つかどうかで条件分岐
if is_invalid:
    print("Yes")
else:
    print(f"{prev_back_text} {new_front_text}")


# しりとり検証用の関数を定義するパターン
# def check_shiritori(words: list[str]) -> tuple[bool, str, str]:
#     prev_last_char = words[0][-1]
#     for current_word in words[1:]:
#         current_first_char = current_word[0]
#         if prev_last_char != current_first_char:
#             return False, prev_last_char, current_first_char
#         prev_last_char = current_word[-1]
#     return True, "", ""

# N = int(input())
# words = [input() in range(N)]

# # しりとりチェック
# is_valid, last_char, next_char = check_shiritori(words)

# if is_valid:
#     print("Yes")
# else:
#     print(f"{last_char} {next_char}")
