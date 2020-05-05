# https://app.codility.com/demo/results/trainingP6QSY6-RJ3/

def solution(A):
    # write your code in Python 3.6
    vals = set()
    
    for n in A:
        vals.add(n)
    
    return len(vals)