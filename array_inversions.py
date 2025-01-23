import copy

#merge sort modifid to count split inversions.
result = []
def merge_sort(arr, l, r):
    if(r-l == 1):
        return 0
    left_inversions = merge_sort(arr, l , (l+r)//2)
    #print(arr[l:(l+r)//2])
    right_inversions = merge_sort(arr,(l+r)//2,r)
    #print(arr[(l+r)//2:r])
    i = l
    j = (l+r)//2
    split_inversions = 0

    for n in range(l,r):
        if(i == (l+r)//2):
            result[n] = arr[j]
            j = j + 1
            continue
        if(j == r):
            result[n] = arr[i]
            i = i + 1
            continue
        if(arr[i] > arr[j]):
            result[n] = arr[j]
            split_inversions = split_inversions + ((l+r)//2) - i
            j = j + 1
        elif(arr[j] >= arr[i]):
            result[n] = arr[i]
            i = i+ 1

    
    for n in range(l,r):
        arr[n] = result[n]
    return (left_inversions + right_inversions + split_inversions)

if __name__=="__main__":
    #arr = [5,1]
    arr = [1, 3, 5, 2, 4, 6]
    l = 0
    r = len(arr)
    result = [0]*r
    inversions = merge_sort(arr,l,r)
    print(arr)
    print(inversions)