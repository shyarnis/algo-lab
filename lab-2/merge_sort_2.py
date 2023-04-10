from generate_input_list import input_list

def merge_sort(A, p, r):
    if p<r:
        q = (p+r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q

    L = [A[p+i] for i in range(n1)] 
    R = [A[q+j+1] for j in range(n2)] 

    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


if __name__ == "__main__":
    unsorted_list = input_list(10)
    n = len(unsorted_list)

    print(f"Before sorting : {unsorted_list}")
    merge_sort(unsorted_list, 0, n-1)
    print(f"After sorting : {unsorted_list}")
