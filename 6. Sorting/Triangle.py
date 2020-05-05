# https://app.codility.com/demo/results/trainingMZSKC5-PQS/
def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N < 3:
        return 0
    
    A.sort()
    
    # if sorted, then gaurantee A[R] + A[Q] > A[P] and A[R] + A[P] > A[Q]. Thus just need to check last condition
    for k in range(N - 2):
        if A[k] + A[k+1] > A[k+2]:
            return 1
    
    return 0
