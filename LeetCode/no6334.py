class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        currentMax = 0
        result = []
        for n in nums:
            currentMax = max(currentMax, n)
            res = currentMax + n

            if not result:
                result.append(res)
            else:
                result.append(result[-1] + res)
        return result
