import random
def quick_sort(arr, l, r):
    if r-l <= 1:
        return
    
    pivot_index = random.randint(l,r-1)
    arr[l], arr[pivot_index] = arr[pivot_index], arr[l]
    seen = unseen = l+1
    for _ in range(l+1, r):
        #if the unseen is LTE than the pivot
        # move it to the left of seen
        if arr[unseen] <= arr[l]:
            arr[seen], arr[unseen] = arr[unseen], arr[seen]
            seen += 1
            unseen += 1
        else:
            unseen += 1

    arr[seen - 1], arr[l] = arr[l],arr[seen - 1]
    quick_sort(arr,seen,r)
    quick_sort(arr,l, seen-1)

if __name__ == "__main__":
    #arr = [5,-5,6,1,2,11,-1,-1,9,3,4,12,0]
    arr = [1,1,1,1,-1,0,2,3,4,-99,1,8,55,3,0,8,3,7,5,-5,6,1,2,11,-1,-1,9,3,4,12,0]
    #arr = [ i for i in range(1000000,0,-1)]
    #random.shuffle(arr)
    quick_sort(arr, 0, len(arr))
    print(arr)
        
