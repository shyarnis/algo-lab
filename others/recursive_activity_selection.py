def RAS(s, f, k, n):
    m = k+1
    while m<=n and s[m] < f[k]:
        m += 1
    
    if m<=n:
        return [m] + RAS(s, f, m, n)
    else:
        return []

if __name__ == "__main__":
    start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish_times = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    k = 0
    total_activities = len(start_times) - 1
    selected_activtives = RAS(start_times, finish_times, k, total_activities)
    print(f"The selected activites numbers are: {selected_activtives}")