def RAS(act, k, n):
    m = k+1
    while m <= n and act[m][0] < act[k][1]:
        m = m+1
    if m <= n:
        return [m] + RAS(act, m, n)
    else:
        return []


s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
k = 0
n = len(s) - 1

act = zip(s, f)

sort_act = sorted(act, key=lambda x: x[1])

print(RAS(sort_act, k, n))
