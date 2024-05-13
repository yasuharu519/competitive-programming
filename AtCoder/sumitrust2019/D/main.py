#!/usr/bin/env python3
def main():
    N = int(input().strip())
    S = input().strip()

    # 次に出てくる文字の最小インデックスを保存しておく
    next_char_map = [[N] * 10 for _ in range(N)]
    last_pos = [N] * 10
    for i in range(N-1, -1, -1):
        next_char_map[i] = last_pos[:]
        digit = int(S[i])
        last_pos[digit] = i
    
    result = 0
    for magic in range(1000):
        magic_str = f"{magic:03}"
        first, second, third = map(int, magic_str)

        first_index = last_pos[first]
        if first_index < N:
            second_index = next_char_map[first_index][second]
            if second_index < N:
                third_index = next_char_map[second_index][third]
                if third_index < N:
                    result += 1
    print(result)
    return

if __name__ == '__main__':
    main()
