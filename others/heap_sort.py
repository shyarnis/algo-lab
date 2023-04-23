def max_heapify(A, i, n):
    l = 2*i+1
    r = 2*i+2

    if l < n and A[l] > A[i]:           # <= raises IndexError
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:     # <= raises IndexError
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, n)    


def build_max_heap(A, n):
    n = len(A) 
    for i in range(n//2, -1, -1):
        max_heapify(A, i, n)


def heap_sort(A):
    n = len(A)
    build_max_heap(A, n)
    for i in range(n-1, 0, -1):         # n-1, n-2, ... , 3, 2, 1
        A[0], A[i] = A[i], A[0]
        n = n - 1
        max_heapify(A, 0, n)


if __name__ == "__main__":
    A = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    heap_sort(A)
    print(A)
