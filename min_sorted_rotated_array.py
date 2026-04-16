def min_sorted_rotated_array(arr):
    high = len(arr) - 1
    low = 0

    if arr[low] <= arr[high]:
        return 0
    
    while low != high:
        mid = (low+high)//2
        if arr[mid] > arr[high]:
            low = mid+1
        else:
            high = mid
    return arr[low]

if __name__ == "__main__":
    arr=[11,12,12,14,-2,-1,6,7,8,9,10]
    print(min_sorted_rotated_array(arr))