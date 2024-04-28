#!/usr/bin/env python3
import math
def main():
    a, b, x = list(map(int, input().strip().split()))

    c = a * a * b
    if c >= x * 2:
        calc = math.atan(a * b * b / (2 * x))
        print(calc * 180 / math.pi)
    else:
        t = 2 * (a * a * b - x)
        calc = math.atan(t / pow(a, 3))
        print(calc * 180 / math.pi)
    
if __name__ == '__main__':
    main()
