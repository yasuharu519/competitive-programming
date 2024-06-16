#!/usr/bin/env python3
def main():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    B = [0] * N

    for i, a in zip(range(N, 0, -1), reversed(A)):
        parity = 0
        x = i * 2
        j = 2
        while x <= N:
            parity = (parity + B[x-1]) % 2
            j += 1
            x = i * j

        if parity == a:
            pass
        else:
            B[i-1] = 1
    
    result = []
    M = 0
    for i in range(N):
        if B[i] == 1:
            result.append(i+1)
            M += 1
    print(M)
    for v in result:
        print(v)
        

if __name__ == '__main__':
    main()
