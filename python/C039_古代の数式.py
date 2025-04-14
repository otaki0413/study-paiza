E = input()
text_list = E.split("+")
sum = 0
for text in text_list:
    sum += text.count("/") * 1 + text.count("<") * 10
print(sum)


# 改善後
def calc_formula(formula: str):
    total = 0
    for t in formula.split(PLUS_MARK):
        ones = t.count(ONE_MARK)
        tens = t.count(TEN_MARK)
        total += ones + tens * 10
    return total


# 定数定義
ONE_MARK = "/"
TEN_MARK = "<"
PLUS_MARK = "+"

formula = input()
result = calc_formula(formula)
print(result)
