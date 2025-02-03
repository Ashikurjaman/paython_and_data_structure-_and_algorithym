"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3"""


def majorityElement(nums):
    n = len(nums)
    
    for i in range(n):
        count = 0
        for j in range (n):
            if nums[j] == nums[i]:
               count+=1
        if count > n//2:
            return nums[i]  
    return -1   
# Using Moore’s Voting Algorithm- O(n) Time and O(1) Space

def majorityElement2(arr):
    n =  len(arr)
    candidate = -1
    count = 0
    for nums in arr:
        if count == 0:
            candidate = nums
            count +=1
        elif nums == candidate:
            count +=1
        else:
            count -=1

    count = 0

    for num in arr:
        if num == candidate:
            count += 1
    if count > n//2:
        return candidate
    else:
        return -1                        
            

nums = [3,2,3]
print(majorityElement(nums))
print(majorityElement2(nums))