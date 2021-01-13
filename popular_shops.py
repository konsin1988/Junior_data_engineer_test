#! /usr/bin/python3

def solve(N, M, visit):
    """
    Determine the positions of the three most popular shops.
    N - positions of shops.
    M - number of persons, who visited shops between numbers of the shops L and R.
    """
    cnt = [0] * N
    for i in range(M):
        l, r = visit[i]
        cnt[l - 1] += 1
        cnt[r - 1] += 1

    for i in range(1, len(cnt) - 1):
        cnt[i] += cnt[i - 1]

    top3 = []
    for _ in range(3):
        top = cnt.index(max(cnt))
        top3.append(top + 1)
        del cnt[top]
    return sorted(top3)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    visit = [list(map(int, input().split())) for i in range(M)]

    out_ = solve(N, M, visit)
    print(' '.join(map(str, out_)))
