def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)
    return arr

def leftRotatebyOne(arr, n):
    tmp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = tmp


arr = [1, 2, 3, 4, 5]
print(leftRotate(arr, 4, 5))