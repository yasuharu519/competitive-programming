import sys


def main():
    N = int(sys.stdin.readline().strip())
    S = sys.stdin.readline().strip()

    start = S[0]
    isMale = start == "M"

    for i in S[1:]:
        if isMale:
            if i == "F":
                isMale = False
                continue
            else:
                print("No")
                break
        else:
            if i == "M":
                isMale = True
                continue
            else:
                print("No")
                break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
