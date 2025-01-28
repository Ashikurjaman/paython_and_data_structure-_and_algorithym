def test_position(cards,query,mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1 >=0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


def locate_card(cards, query):
    lo, high = 0, len(cards) - 1
    
    while lo <= high:
        mid = (lo + high) // 2
        mid_number = cards[mid]
        print('lo:', lo, ', high:', high, ', mid:', mid, ', mid_number:', mid_number)
        result = test_position(cards,query,mid)
        
        if result == 'found':
            return mid
        elif result == 'left':  # Move left in the sorted (descending) list
            high = mid - 1
        elif result == 'right':  # Move right in the sorted (descending) list
            lo = mid + 1  
    return -1  

# Test Cases
test_cases = [
    {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7, "expected": 3},   # Case: Number exists in the middle
    {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 1, "expected": 6},   # Case: Number exists at the end
    {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 13, "expected": 0},  # Case: Number exists at the start
    {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 5, "expected": -1},  # Case: Number does not exist
    {"cards": [], "query": 7, "expected": -1},                          # Case: Empty list
    {"cards": [4], "query": 4, "expected": 0},                          # Case: Single element, query matches
    {"cards": [4], "query": 7, "expected": -1}                          # Case: Single element, query does not match
]

# Run Test Cases
for i, test in enumerate(test_cases, 1):
    result = locate_card(test["cards"], test["query"])
    print(f"Test Case {i}: {'Pass' if result == test['expected'] else 'Fail'}, Output: {result}")
