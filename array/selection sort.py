def selection_sort(arr):
    for i in range(len(arr)-1):
        print(i +1,'pas',end=" ")
        min_index = i
        print(min_index)

        for j in range(i + 1 , len(arr)):
            print("current observation item",arr)
            if arr[j] < arr[min_index]:
                print("current item is less then min",arr[j])
                min_index = j
                print("current  min",arr[min_index])
        arr[i],arr[min_index] = arr[min_index],arr[i]
        print(arr)    
    return arr

arr = [64,25,12,22,11]    
sorted_arr = selection_sort(arr)
print(sorted_arr)

