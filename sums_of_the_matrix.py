#! /usr/bin/python3


def solve(A, queries):
    """
    Count total number of raws and columns,
    which have their sum in [L, R].
    Q queries with left L and right R.
    """
    S_column = [0] * N
    S_row = [0] * M
    for i in range(M):
        for j in range(N):
            S_column[j] += A[i][j]
            S_row[i] += A[i][j]

    out_ = [0] * queries_num
    for i in range(queries_num):
        for j in range(N):
            if queries[i][0] <= S_column[j] <= queries[i][1]:
                out_[i] += 1
        for k in range(M):
            if queries[i][0] <= S_row[k] <= queries[i][1]:
                out_[i] += 1

    return out_

N = int(input())
M = int(input())
A = []
queries = []

for i in range(M):
    A.append(list(map(int, input().split())))

queries_num = int(input())
assert input() == '2'

for i in range(queries_num):
    queries.append(tuple(map(int, input().split())))

out_ = solve(A, queries)
print(*out_)
