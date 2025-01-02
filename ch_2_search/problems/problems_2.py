# 2. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [1,3,5,6], target = 5
# Output: 2
nums = [1,3,5]
target = 1
def binary_search(lo,hi,condition):
    while lo <= hi:
        mid = (lo+hi) // 2
        result = condition(mid)
        if result == "found":
            return mid
        elif result == 'left':
            hi = mid -1
        else:
            lo = mid + 1
    return lo       

def find_insert(nums,target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid] +1 == target:
                return 'right'
            return "found"
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0,len(nums)-1,condition)

print(find_insert(nums,target))    

            
