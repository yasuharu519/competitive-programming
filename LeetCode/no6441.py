class Solution:

    def search(self, currentNum: int, squareStr: str, target: int,
               startPos: int) -> bool:
        n = len(squareStr)
        if startPos >= n:
            return currentNum == target

        if currentNum > target:
            return False

        for i in range(1, len(squareStr) + 1 - startPos):
            taken = int(squareStr[startPos:startPos + i])
            res = self.search(currentNum + taken, squareStr, target,
                              startPos + i)
            if res:
                return True
        return False

    def isPanishmentNum(self, n: int) -> bool:
        target = n**2
        squareStr = str(target)

        for i in range(1, len(squareStr) + 1):
            cur = int(squareStr[:i])
            res = self.search(cur, squareStr, n, i)
            if res:
                return True

        return False

    def punishmentNumber(self, n: int) -> int:
        if n < 9:
            return 1
        elif n < 10:
            return 82
        elif n < 36:
            return 182
        elif n == 36:
            return 1478
        else:
            sum = 1478
            for i in range(37, n + 1):
                if self.isPanishmentNum(i):
                    sum += i**2
            return sum


if __name__ == "__main__":
    s = Solution()
    # 3503
    # print(s.isPanishmentNum(45))
    print(s.punishmentNumber(45))