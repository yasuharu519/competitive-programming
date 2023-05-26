import math
from functools import cache
from typing import List


class Solution:

    @cache
    def gcd(self, numA: int, numB: int) -> int:
        return math.gcd(numA, numB)

    def minOperations(self, nums: List[int]) -> int:
        v = self.minOperationsImpl(nums)
        return -1 if v == float('inf') else v

    def minOperationsImpl(self, nums: List[int]) -> int:
        if all([x == 1 for x in nums]):
            return 0

        if 1 in nums:
            return len([x for x in nums if x != 1])

        @cache
        def calc(index: int, value: int) -> int:
            target = nums[:index] + [value] + nums[index + 1:]
            if all([x == 1 for x in target]):
                return 0
            if 1 in target:
                return len([x for x in target if x != 1])
            n = len(target)
            result = float('inf')
            for i in range(n - 1):
                gcd = self.gcd(target[i], target[i + 1])
                print(i, gcd)

                if gcd != target[i]:
                    result = min(result, calc(i, gcd) + 1)
                if gcd != target[i + 1]:
                    result = min(result, calc(i + 1, gcd) + 1)
            return result

        n = len(nums)
        result = float('inf')
        for i in range(n - 1):
            gcd = self.gcd(nums[i], nums[i + 1])
            print(i, gcd)

            if gcd != nums[i]:
                result = min(result, calc(i, gcd) + 1)
            if gcd != nums[i + 1]:
                result = min(result, calc(i + 1, gcd) + 1)
        return result


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.minOperations([
            715086, 420033, 320095, 230175, 359910, 99010, 261428, 561978,
            495675, 817898
        ]))
