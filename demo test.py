
def solution(A):
    # write your code in Python 3.6
    # remove negative values and sort in ascending order
    A = sorted(list(filter(lambda x: x > 0, A)))
    if len(A) == 0:
        # A only had negative values
        return 1
    else:
        if min(A) > 1:
            # min value is bigger than 1
            return 1
    for i in range(len(A) - 1):
        if A[i+1] - A[i] > 1:
            return A[i] + 1
    return A[-1] + 1

B = [1, 2, 3, 5]
print(solution(B))