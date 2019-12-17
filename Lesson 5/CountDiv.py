def solution(A, B, K):
    # write your code in Python 3.6
    if A%K == 0:
        return 1+(B-A)//K
    else: 
        return (B - (A - A%K))//K