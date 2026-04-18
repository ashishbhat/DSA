def solution(arr: list) -> list:
    N = len(arr)
    stack = list()
    result = [-1]*N

    for i in range(2*N):
        while stack and arr[i%N] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i%N]
        stack.append(i%N) if result[i % N] == -1 else None
                
    return result

if __name__ == "__main__":
    arr = [11,1,2,0,1,3,4,5,0,3,5,6,2,1,4,10,0]
    print(arr)
    print(solution(arr))


# if stack is empty -> push current position
# if current value < arr[tos] -> push
# if current > arr[tos] -> pop while current > arr[tos] and push current index