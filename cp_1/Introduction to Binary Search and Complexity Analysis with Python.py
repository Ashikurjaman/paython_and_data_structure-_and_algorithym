'''QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.'''
cards = [12,11,10,9,8,7,6,5,4,3,2,1]
query = 4


# def bianry_search(lo,hi,condition):
#     cycle = 0
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         result= condition(mid)
#         print("lo:", lo, ", hi:", hi, ", mid:", mid)
#         if result == "found":
#             print("Total cycles:", cycle + 1)  # To include the last cycle
#             return mid
#         elif result == "left":
#              hi = mid - 1
#         else:
#             lo = mid + 1 
#         cycle +=1   
#     print(cycle)        
#     return -1       

# def locate_card(cards,query):
#     def condition(mid):
#         if cards[mid] == query :
#             if mid > 0 and cards[mid-1] == query:
#                 return "left"
#             else: 
#                 return "found"
#         elif cards[mid] < query:
#             return "left"
#         else:
#             return "right"  
   
#     return bianry_search(0,len(cards)-1,condition)    

# print("Index of the card:", locate_card(cards, query))


# import unittest

# class TestLocateCard(unittest.TestCase):

#     def test_target_exists_single_occurrence(self):
#         cards = [12, 11, 10, 9, 8, 7, 4, 5, 6, 2, 1]
#         query = 11
#         self.assertEqual(locate_card(cards, query), 1)

#     def test_target_exists_multiple_occurrences(self):
#         cards = [12, 11, 11, 11, 9, 8, 7]
#         query = 11
#         self.assertEqual(locate_card(cards, query), 1)  # Should return the first occurrence

#     def test_target_does_not_exist_smaller_than_all(self):
#         cards = [12, 11, 10, 9, 8]
#         query = 1
#         self.assertEqual(locate_card(cards, query), -1)

#     def test_target_does_not_exist_larger_than_all(self):
#         cards = [12, 11, 10, 9, 8]
#         query = 15
#         self.assertEqual(locate_card(cards, query), -1)

#     def test_empty_array(self):
#         cards = []
#         query = 5
#         self.assertEqual(locate_card(cards, query), -1)

#     def test_single_element_array_found(self):
#         cards = [11]
#         query = 11
#         self.assertEqual(locate_card(cards, query), 0)

#     def test_single_element_array_not_found(self):
#         cards = [11]
#         query = 10
#         self.assertEqual(locate_card(cards, query), -1)

#     def test_all_identical_elements(self):
#         cards = [7, 7, 7, 7]
#         query = 7
#         self.assertEqual(locate_card(cards, query), 0)  # Should return the first index

#     def test_all_identical_elements_not_found(self):
#         cards = [7, 7, 7, 7]
#         query = 5
#         self.assertEqual(locate_card(cards, query), -1)

# if __name__ == "__main__":
#     unittest.main()




# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
                   

def binary_search (lo,hi,condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1   


def searchNums(nums,target):
    def condition(mid):
        if nums[mid] == target:
            if mid > len(nums) - 1 and nums[mid + 1] == target:
                return "right"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0,len(nums)-1,condition)

 
nums = [2,7,11,15], target = 9

