def LCS_length(A, B):
    m = len(A)
    n = len(B)
    len = [[0]*(n+1) for _ in range(m+1)]
    prev = [[0]*(n+1) for _ in range(m+1)]

    # for i in range(0, m+1):
    #     len[i][0] = 0
    len = [len[i][0] for i in range(0, m+1)]
    
    len[0] = [0 for _ in range(1, n+1)]

    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                len[i, j] = len[i-1][j-1] + 1
                prev[i][j] = -1     # diagonal arrow
            # elif
            elif len[i-1][j] >= len[i][j-1]:
                len[i][j] = len[i-1][j]
                prev[i][j] = 0      # upward arrow
            else:
                len[i][j] = len[i][j-1]
                prev[i][j] = 1      # forward arrow
    
    return len and prev

def ouptut_LCS(A, prev, i, j):
    if not i or not j:
        return 
    
    if prev[i][j] == -1:            # diagonal arrow
        ouptut_LCS(A, prev, i-1, j-1)
        print(A[i-1])
    elif prev[i][j] == 0:           # upward arrow
        ouptut_LCS(A, prev, i-1, j)
    else:
        ouptut_LCS(A, prev, i, j-1)

if __name__ == "__main__":
    # use input here
    A = input("Enter A : ")     # president
    B = input("Enter B : ")     # providence
    m = len(A)
    n = len(B)

    len, prev = LCS_length(A, B)
    ouptut_LCS(A, B, m, n)