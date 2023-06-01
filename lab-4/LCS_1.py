def LCS_length(A, B):
    m = len(A)
    n = len(B)
    length = [[0]*(n+1) for _ in range(m + 1)]
    prev = [[0]*(n+1) for _ in range(m + 1)]

    for i in range(1, m+1):
        for j in range(1, n+1):

            if A[i-1] == B[j-1]:
                
                length[i][j] = length[i-1][j-1] + 1
                prev[i][j] = 2             # diagonal arrow
            
            elif length[i-1][j] >= length[i][j-1]:

                length[i][j] = length[i-1][j]
                prev[i][j] = 3              # upward arrow
            
            else:
                
                length[i][j] = length[i][j-1]
                prev[i][j] = 4              # forward arrow

    return length, prev


def output_LCS(A, prev, i, j):
    if i == 0 or j == 0:
        return

    if prev[i][j] == 2:                     # diagonal arrow
        # print(A[i-1], end= "")              # to print in reverse order
        output_LCS(A, prev, i-1, j-1)
        print(A[i-1], end= "")

    
    elif prev[i][j] == 3:                   # upward arrow
        output_LCS(A, prev, i-1, j)
    
    else:
        output_LCS(A, prev, i, j-1)


if __name__ == "__main__":
    A = input("Enter A: ")
    B = input("Enter B: ")

    length, prev = LCS_length(A, B)
    output_LCS(A, prev, len(A), len(B))
    
    max_length = max(max(i) for i in length)
    print(f"\nThe Longest Common Subseqeunce is of length {max_length}")
