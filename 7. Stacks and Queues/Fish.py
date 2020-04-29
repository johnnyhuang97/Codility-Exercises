# https://app.codility.com/demo/results/trainingVKJR3W-P6R/

def solution(A, B):
    # write your code in Python 3.6
    stack = []
    N = len(A)
    for fish in range(N):
        if not stack:
            stack.append(fish)
            continue
        prev_fish = stack[-1]
        if B[fish] == B[prev_fish] or not B[prev_fish]:
            stack.append(fish)
        else:
            while stack and B[stack[-1]]:
                if A[fish] > A[stack[-1]]:
                    stack.pop()
                else:
                    fish = -1
                    break
            
            if fish >= 0:
                stack.append(fish)
    
    return len(stack)