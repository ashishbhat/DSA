
def solution(s : str) -> str:
    N = len(s)
    seen = dict()
    left = 0
    start = end = 0
    for right in range(0,N):
        element = s[right]
        if element in seen:
            if seen[element] >= left:
                left = seen[element] + 1
 
        if right - left > end - start:
            start, end = left, right
        seen[element] = right 

    return s[start:end+1]

if __name__ == "__main__":
    #s = '12345656567890123'
    s = 'abcabcad'
    print(solution(s.replace(' ','')))

