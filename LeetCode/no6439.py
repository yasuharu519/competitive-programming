class Solution:

    def hasABCD(self, s: str) -> int:
        if "AB" in s:
            return s.find("AB")
        elif "CD" in s:
            return s.find("CD")
        return -1

    def minLength(self, s: str) -> int:
        current = s
        pos = self.hasABCD(current)

        while pos != -1:
            current = current[:pos] + current[pos + 2:]
            pos = self.hasABCD(current)

        return len(current)
