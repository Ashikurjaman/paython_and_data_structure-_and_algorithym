def linear_search(arr,item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1


arr = [22,23,29,1,5,48,75]
print(linear_search(arr,121))