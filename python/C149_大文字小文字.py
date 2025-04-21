S = input()
T = input()

part_list = []
for part in T:
    # ルール表に含まれない場合は変換
    if part not in S:
        if part.islower():
            convert_part = part.upper()
        else:
            convert_part = part.lower()
    else:
        convert_part = part
    part_list.append(convert_part)


print("".join(part_list))


# -----------------------
# 別解
def correct_text(rule: str, text: str) -> str:
    part_list = []
    for part in text:
        if part not in rule:
            part_list.append(part.swapcase())
        else:
            part_list.append(part)
    return "".join(part_list)


def main():
    rule = input()  # 校正ルール表
    text = input()  # 校正対象テキスト
    result = correct_text(rule, text)
    print(result)


"ABcDef".swapcase()  # abCdEF
