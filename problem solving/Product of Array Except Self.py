### **Problem Explanation**

# Given an integer array `nums`, return an array `result` such that `result[i]` is equal to the product of all elements of `nums` except `nums[i]`.

# **Example**:

# Input: `nums = [1, 2, 3, 4]`

# Output: `[24, 12, 8, 6]`


def calculateArrayExceptSelf(nums):
    n = len(nums)
    res = [1] * n
    print(res)
    pro = 1

    for i in range(n):
        pro = 1
        for j in range(n):
            if nums[i] == nums[j]:
                continue

            pro *= nums[j]
        res[i] = pro    

    return res        


def cal1(num):
    n = len(num)
    rtl = [1] * n

    product = 1
    for i in range(n-1,-1,-1):
        rtl[i] = product
        product *= num[i]
        

    product = 1
    for i in range(1,n):
        rtl[i] *= product
        product *=num[i]
       
    return rtl         

num = [-1,1,0,-3,3]
print(cal1(num))
print(calculateArrayExceptSelf(num))