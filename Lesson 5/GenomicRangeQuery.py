def count_slice(A, x, y):
    return A[y] - A[x - 1]
    
def solution(S, P, Q):
    N = len(S)
    mapping = {'A':1, 'C':2, 'G':3, 'T':4}
    
    dp = [[0] * (N + 1), [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)]
    
    for i in range(1, N + 1):
        for j in range(4):
            dp[j][i] = dp[j][i-1]
        dp[mapping[S[i - 1]]-1][i] += 1
    
    for i in range(len(P)):
        l = P[i] + 1
        r = Q[i] + 1
        if count_slice(dp[0], l, r) > 0:
            P[i] = 1
        elif count_slice(dp[1], l, r) > 0:
            P[i] = 2
        elif count_slice(dp[2], l, r) > 0:
            P[i] = 3
        elif count_slice(dp[3], l, r) > 0:
            P[i] = 4
        else:
            P[i] = mapping[S[P[i]]]
            
    
    return P