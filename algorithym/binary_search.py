def located_card(cards,query):
    pass

cards = [13,11,10,7,4,3,1,0]
query = 7
output = 3

result = located_card(cards,query)
print(result)

print(result == output)






test ={
    'input':{
        'cards':[13,11,10,7,4,3,1,0],
        'query': 7
    },
    'output':3
}

print(located_card(**test['input']) == test['output'])

tests = []
tests.append(test)

tests.append(
    {
    'input':{
        'cards':[13,11,10,7,4,3,1,0],
        'query': 1
    },
    'output':6
}
)
tests.append(
    {
    'input':{
        'cards':[4,2,1,-1],
        'query': 4
    },
    'output':0
}
)
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})
# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})
print(tests)