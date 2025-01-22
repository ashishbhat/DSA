import copy

result = []
def merge_sort(arr, l, r):
    if(r-l == 1):
        return
    merge_sort(arr, l , (l+r)//2)
    #print(arr[l:(l+r)//2])
    merge_sort(arr,(l+r)//2,r)
    #print(arr[(l+r)//2:r])
    i = l
    j = (l+r)//2

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
            j = j + 1
        elif(arr[j] >= arr[i]):
            result[n] = arr[i]
            i = i+ 1

    
    for n in range(l,r):
        arr[n] = result[n]

if __name__=="__main__":
    #arr = [5]
    arr = [8,7,6,5,4,3,2,0,2]
    l = 0
    r = len(arr)
    result = [0]*r
    merge_sort(arr,l,r)
    print(arr)