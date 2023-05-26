class Solution:

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        dp = [0] * 51
        result = []

        def findKthMin() -> int:
            count = 0
            for i in range(50, -1, -1):
                count += dp[i]
                if count >= x:
                    return -1 * i
            return 0

        for i, v in enumerate(nums):
            if v >= 0:
                dp[0] += 1
            else:
                dp[v * -1] += 1

            if i < k - 1:
                continue
            elif i == k - 1:
                result.append(findKthMin())
            else:
                backValue = nums[i - k]
                if backValue >= 0:
                    dp[0] -= 1
                else:
                    dp[backValue * -1] -= 1
                result.append(findKthMin())
        return result
