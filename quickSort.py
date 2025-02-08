def quick_sort(arr,l,r):
    if(r-l <= 1):
       return

    pivot_index = (r+l)//2
    arr[l], arr[pivot_index] = arr[pivot_index], arr[l]

    i = l+1
    for j in range(l+1,r):
       if(arr[j] <= arr[l]):
          arr[i],arr[j] = arr[j],arr[i]
          i = i +1
    arr[l],arr[i-1] = arr[i-1],arr[l]

    new_partition = i - 1
    quick_sort(arr,l,new_partition)
    quick_sort(arr,new_partition+1,r)

    return arr

if __name__=="__main__":
  arr = [8,9,7,6,5,4,3,2,1,-1,0,0,0,1]
  l = 0
  r = len(arr)
  print(quick_sort(arr,l,r))