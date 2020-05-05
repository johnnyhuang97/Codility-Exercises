# https://app.codility.com/demo/results/trainingJ35Q9W-UQ8/
# 
def solution(A):
    # write your code in Python 3.6
    A.sort()
    
    # All negative: -3:-1
    # All positive: -3:-1
    # Mixed: max([0, 1, -1],[-3: -1])
    return max(A[-3]*A[-2]*A[-1], A[0]*A[1]*A[-1])