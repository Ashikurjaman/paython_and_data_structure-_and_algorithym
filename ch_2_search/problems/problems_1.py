# 1.Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# nums = [5,7,7,9,9,10] 
nums = [0,0,1,2,2]
target = 2

def binary_search(lo,hi,condition):
    position = -1
    while lo<=hi:
        mid = (lo+hi) // 2
        result = condition(mid)
        if result == "found":
            position = mid
            return position
        elif result == "left":
            hi = mid - 1
        else:
            lo = mid + 1
    return position
def search_int(nums,target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid -1] == target:
                return "left"
            return 'found'
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0,len(nums)-1,condition)

def search_2nd_int(nums,target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid +1] == target:
                return "right"
            return 'found'
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0,len(nums)-1,condition)
        

first_position = search_int(nums, target)
second_position = search_2nd_int(nums, target)
print([first_position,second_position])