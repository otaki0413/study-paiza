S = input()

result = []
prev_part = ""
for part in S:
    # 文字がハイフンかつ前の文字がハイフン出ない場合、スキップ
    if part == "-" and prev_part == "-":
        continue
    result.append(part)
    prev_part = part

print("".join(result))


# スキップさせる条件ではなく、出力対象の文字を格納していくロジックの場合
S = input()

result = []
prev_part = ""
for part in S:
    if part != "-":
        result.append(part)
    elif prev_part != "-":
        result.append(part)
    prev_part = part

print("".join(result))
