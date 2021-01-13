#! /usr/bin/python3

def numbers(N, tmp, comb):      # N = len(str(samples[i]))
    """
    Give a list contains only special numbers.
    Decimal representation of special number: 4, 5, 44, 45, 54, 55, 444, 445, etc.
    """
    if N == 0:
        return
    tmp.append('4')
    comb.append(''.join(tmp))
    numbers(N-1, tmp, comb)
    tmp.pop()
    tmp.append('5')
    comb.append(''.join(tmp))
    numbers(N-1, tmp, comb)
    tmp.pop()
    return

def solve (T, samples):
    """
    Find a single number denoting the minimum number of special numbers 
    whose sum is equal to N. if it is impossible, print -1.
    Decimal representation of special number: 4, 5, 44, 45, 54, 55, 444, 445, etc.
    """
    out_ = []
    for i in range(len(samples)):
        comb = []
        tmp = []
        numbers(len(str(samples[i])), tmp, comb)
        comb = list(map(int, comb))
        comb = [x for x in comb if x <= samples[i]]
        if comb == []:
            out_.append(-1)
            continue
        F = [[-1] * len(comb) for _ in range(samples[i] + 1)]

        for k in range(1, samples[i] + 1):
            for j in range(len(comb)):
                if comb[j] == k:
                    F[k][j] = 1
                elif k > comb[j]:
                    if max(F[k - comb[j]][:j + 1]) > 0:
                        F[k][j] = 1 + min([x for x in F[k - comb[j]] if x > 0])
                    else:
                        continue

        if max(F[samples[i]]) > 0:
            out_.append(min([x for x in F[samples[i]] if x > 0]))
        else:
            out_.append(-1)
    return out_


T = int(input())
samples = []
for _ in range(T):
    samples.append(int(input()))

out_ = solve (T, samples)
print('\n'.join(map(str, out_)))
