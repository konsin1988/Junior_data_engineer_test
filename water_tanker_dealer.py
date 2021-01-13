#! /usr/bin/python3

def solve(water, capacity):
    """
    Count min number of tanks, required to transport the total amount
    of water to another city. 
    N - total amount of tanks.
    C - capacity of each tank.
    W - amount of water present in each tank
    """
    F = [[0] * (len(capacity) + 1) for i in range(sum(water) + 1)]
    for i in range(1, sum(water) + 1):
        for j in range(1, len(capacity) + 1):
            print(f'{capacity[j - 1]} - {i}')

            if capacity[j-1] >= i:
                F[i][j] = 1
            else:
                F[i][j] = 1 + min(F[i - capacity[j - 1]][1:])
    print(F)

    return min(F[sum(water)][1:])



n = int(input())
capacity = list(map(int, input().split()))
water = list(map(int, input().split()))
print(water)
print(capacity)
print(sum(water))


out_ = solve(water, capacity)
print(out_)
