from generate_random_list import rand_list

def insertion_sort(A):
    n = len(A)

    for j in range(1, n):
        key = A[j]
        i = j-1

        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    
    return A


if __name__ == "__main__":
    unsorted_list = rand_list(100)
    print(f"Before sorting : {unsorted_list}")

    sorted_list = insertion_sort(unsorted_list)
    print(f"After sorting : {sorted_list}")

