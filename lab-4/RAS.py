def RAS(act, k, n):
    m = k+1
    while m <= n and act[m][0] < act[k][1]:
        m += 1
    if m <= n:
        return [(s[m], f[m])] + RAS(act, m, n)
    else:
        return []
    

if __name__ == "__main__":
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    k = 0
    n = len(s) - 1

    act = zip(s, f)
    sorted_act = sorted(act, key=lambda x: x[1])

    selected_activites = RAS(sorted_act, k, n)
    print(f"The selected activites = {selected_activites}")

    for activites in selected_activites:
        start, finish = activites
        print(f"start time: {start}, finish time: {finish}")