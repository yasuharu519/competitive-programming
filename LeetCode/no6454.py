class Solution:

    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        result = list(s)

        for i in range(n // 2):
            if s[i] == s[-(i + 1)]:
                continue
            else:
                if s[i] < s[-(i + 1)]:
                    result[-(i + 1)] = s[i]
                else:
                    result[i] = s[-(i + 1)]
        return "".join(result)
