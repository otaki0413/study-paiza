def main():
    N = int(input())
    S1 = input().strip()
    S2 = input().strip()

    doubled = S1 + S1
    if S2 in doubled:
        print("Yes")
    else:
        print("No")


main()
