def search(arr, target, low, high):
    assert arr == sorted(arr), "Array must be sorted"

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

arr = [1, 2, 5, 9, 23, 78]
result = search(arr, 78, 0, len(arr) - 1)
if result == -1:
    print("Not found")
else:
    print(f'FOUND AT POSITION: {result + 1}')



