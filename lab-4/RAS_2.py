def RAS(s, f, k, n):
    m = k + 1
    
    while m<=n and s[m] < f[k]:
        m += 1
    
    if m <= n:
        return [(s[m], f[m])] + RAS(s, f, m ,n)
    else:
        return []
    
if __name__ == "__main__":
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    k = 0
    n = len(s) - 1

    selected_act = RAS(s, f, k ,n)
    print(f"The selected activites are {selected_act}")

    for act in selected_act:
        start, finish = act
        print(f"start time: {start}, finish time: {finish}")
