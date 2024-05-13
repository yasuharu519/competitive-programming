#!/usr/bin/env python3
import bisect

MOD = pow(10, 8)

def main():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    A.sort()
    
    passed_nums = [A[0]]
    passed_sum = A[0]
    result = 0
    over_num  = 0

    for a in A[1:]:
        rest = MOD - a
        over_num += len(passed_nums) - bisect.bisect_left(passed_nums, rest)
        result += (a * len(passed_nums) + passed_sum)
        passed_nums.append(a)
        passed_sum += a
    
    print(result - MOD * over_num)


if __name__ == '__main__':
    main()
