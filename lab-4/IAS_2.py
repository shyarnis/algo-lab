def IAS(s, f):
    n = len(s)
    A = []
    k = 0

    for m in range(1, n):
        if s[m] >= f[k]:
            A.append(m)
            k = m
    return A

if __name__ == "__main__":
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    selected_act = IAS(s, f)
    print(f"Selected Activities: {selected_act}")

    for act in selected_act:
        start, finish = s[act], f[act]
        print(f"start time: {start}, finish time: {finish}")
