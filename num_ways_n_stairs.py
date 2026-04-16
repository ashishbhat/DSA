def solution(N, cache=None):
    if N == 0:
        return 1
    if N == 1:
        return 1
    if N == 2:
        return 2
    
    if cache is None:
        cache = dict()
    if N in cache:
        return cache[N]
    cache[N] = solution(N-3, cache)+solution(N-2, cache)+solution(N-1, cache)
    return cache[N]

def solution_non_recursive(N):
    cache = {0:1, 1:1, 2:2}

    for i in range(3, N+1):
        cache[i] = cache[i-1] + cache[i-2] + cache[i-3]
    
    return cache[N]

n = 5
print(solution(n)) 
print(solution_non_recursive(n))