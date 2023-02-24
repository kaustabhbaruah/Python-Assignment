
def binary_search(list, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if list[mid] == x:
            return mid+1
        elif list[mid] > x:
            return binary_search(list, low, mid - 1, x)
        else:
            return binary_search(list, mid + 1, high, x)
    else:
        return -1
list = [9, 99, 999, 9999, 99999, 100000]
x = 100000
result = binary_search(list, 0, len(list)-1, x)
 
if result != -1:
    print("Element is present at index: {}".format(result))
else:
    print("Element is not present in the list")