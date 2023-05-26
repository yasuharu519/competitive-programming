class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) % 3 != 0:
            return False
        for i in range(0, len(word), 3):
            if word[i:i+3] != "abc":
                return False
        return True

    def addMinimum(self, word: str) -> int:
        if self.isValid(word):
            return 0
        if word[0:3] == "abc":
            return self.addMinimum(word[3:])
        if word[0:2] == "ab":
            return 1 + self.addMinimum(word[2:])
        if word[0:2] == "ac":
            return 1 + self.addMinimum(word[2:])
        if word[0:2] == "bc":
            return 1 + self.addMinimum(word[2:])
        if word[0:1] == "a":
            return 2 + self.addMinimum(word[1:])
        if word[0:1] == "b":
            return 2 + self.addMinimum(word[1:])
        if word[0:1] == "c":
            return 2 + self.addMinimum(word[1:])
        return 3

        