class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors.sort()

        maxScore = 0
        maxDivisor = divisors[0]

        for d in divisors:
            count = 0
            for n in nums:
                if n % d == 0:
                    count += 1
            if count > maxScore:
                maxScore = count
                maxDivisor = d

        if maxScore == 0:
            return min(divisors)
        else:
            return maxDivisor
