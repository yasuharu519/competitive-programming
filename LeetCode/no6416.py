class Solution:

    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = []
        for i in range(1, n + 1):
            prefix, suffix = nums[:i], nums[i:]
            p, q = len(set(prefix)), len(set(suffix))
            res.append(p - q)

        return res
