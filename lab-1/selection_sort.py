from generate_random_list import rand_list

def selection_sort(A):
    n = len(A)

    for i in range(n):
        m = i

        for j in range(i+1, n):
            if A[j] < A[m]:
                m = j

        A[i], A[m] = A[m], A[i]

    return A


if __name__ == "__main__":
    unsorted_list = rand_list(100)
    print(f"Before sorting : {unsorted_list}")

    sorted_list = selection_sort(unsorted_list)
    print(f"After sorting : {sorted_list}")

