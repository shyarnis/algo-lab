def IAS(s, f):
    n = len(s)
    A = []
    k=0
    for m in range(1, n):
        if s[m] >= f[k]:
            A.append(m)
            k = m
    return A

if __name__ == "__main__":
    start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish_times = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    selected_activtives = IAS(start_times, finish_times)
    print(f"The selected activites numbers are: {selected_activtives}")