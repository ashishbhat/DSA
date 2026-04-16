def sokrati(arr,R,C,r=0, path=None):
    if path is None:
        path = []

    if r == R:
        print(path)
        return
    
    for c in range(0,C):
        sokrati(arr,R,C,r+1,path + [arr[r][c]])
    

x = [[1,2,3,5],
    [5,6,7,8],
    [9,10,11,12]]
sokrati(x,3,4)