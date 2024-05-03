#!/usr/bin/env python3
from collections import Counter
def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))

    even_counter = Counter([x for i, x in enumerate(v) if i % 2 == 0])
    odd_counter = Counter([x for i, x in enumerate(v) if i % 2 == 1])
    even_values = sorted([(v, k) for k, v in even_counter.items()], reverse=True)
    odd_values = sorted([(v, k) for k, v in odd_counter.items()], reverse=True)

    if even_values[0][1] == odd_values[0][1]:
        change1 = n - even_values[0][0] - (odd_values[1][0] if len(odd_values) > 1 else 0)
        change2 = n - odd_values[0][0] - (even_values[1][0] if len(even_values) > 1 else 0)
        print(min(change1, change2))
    else:
        print(n - even_values[0][0] - odd_values[0][0])

if __name__ == '__main__':
    main()
