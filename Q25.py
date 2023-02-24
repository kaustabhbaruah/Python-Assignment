
def SelectionSort(arr):
    for i in range(len(arr)): 
        mini = i 
        for j in range(i+1, len(arr)): 
            if arr[mini] > arr[j]: 
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
arr = [26, 14, 65, 1, 3, 7]
print("Initial Array: {}".format(arr))
SelectionSort(arr)
print ("Sorted array is : {}".format(arr))