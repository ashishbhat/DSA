import random
def sort(arr):
    N = len(arr)

    for i in range(N-1):
        min_index = i
        for j in range (i+1,N):
            if(arr[min_index] > arr[j]):
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

if __name__ == "__main__":
    #arr = [random.randint(-500, 500) for _ in range(5)]
    arr = [8,7,6,5,4,3,2,1]
    sort(arr)
    print(arr)