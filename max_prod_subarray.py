from functools import reduce
def max_prod_subarray(arr : list) -> list:
    result = arr[0]
    max_prod = min_prod = arr[0]

    for i in range(1,len(arr)):
        temp_max = max_prod
        max_prod = max(arr[i], max(arr[i]*temp_max, arr[i]*min_prod))
        min_prod = min(arr[i], min(arr[i]*temp_max, arr[i]*min_prod))

        result = max(result, max_prod)

    return result

def max_prod_subarray2(arr : list) -> list:
    N = len(arr)
    max_prod = arr[0]
    left_prod = right_prod = 1
    for i in range(0, N):
        left_prod *= arr[i]
        right_prod *= arr[N-1-i]
        max_prod =  max(left_prod,right_prod,max_prod )
    return max_prod

    prod = 1
    for i in range(len(arr)-1,-1,-1):
        prod *= arr[i]
        max_prod = max(max_prod,prod)

    return max_prod


if __name__ == "__main__":
    inputs =    [[-1, 0, -1 ,-1 ,-1],
                [-2, -2, -2],
                [-2, 1, -2,-2,6],
                [1,2,0,3,-4,5,6,-7],
                [1,2,3,-4,5,6,],
                [-2,1,-2, -2, 6],
                [-1,0]]
    
    for x in inputs:
        print(f'{x} -> {max_prod_subarray2(x)}')