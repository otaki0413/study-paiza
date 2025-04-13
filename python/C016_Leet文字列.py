LEET_MAP = {
    "A": "4",
    "E": "3",
    "G": "6",
    "I": "1",
    "O": "0",
    "S": "5",
    "Z": "2",
}
S = input()
result = []

for part in S:
    replaced_part = LEET_MAP.get(part, part)
    result.append(replaced_part)

print("".join(result))
