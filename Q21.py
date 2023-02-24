def BubbleSort(arr):
    x = len(arr)
    for i in range(x):
        for j in range(0, x-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [10, 15, 1, 5, 99, 6, 0]
print("Initial Array: {}".format(arr))
BubbleSort(arr)
print ("The sorted Array is = {}".format(arr))