def solution(S):
    # write your code in Python 3.6
    map_left = {"(": 1, "[": 2, "{": 3}
    map_right = {")": 1, "]": 2, "}": 3}
    
    stack = []
    
    for i in range(len(S)):
        val = S[i]
        if val in map_left:
            stack.append(val)
        elif val in map_right:
            if not stack:
                return 0
            left = stack.pop()
            if map_left[left] != map_right[val]:
                return 0
    
    if stack:
        return 0
    return 1