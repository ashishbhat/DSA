import random
def sort(arr):
    N = len(arr)

    for i in range(1,N):
        for j in range (i,0,-1):
            if(arr[j] < arr[j-1]):
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break

if __name__ == "__main__":
    arr = [random.randint(-500, 500) for _ in range(20000)]
    #arr = [-8,7,6,5,4,3,2,1,0,-1,7,9,0,12,-9]
    sort(arr)
    print(arr)