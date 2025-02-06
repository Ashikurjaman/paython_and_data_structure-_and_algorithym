# String1 = 'Welcome to the Geeks World'
# print("String with the use of Single Quotes: ")
# # print(String1)
# String1 = '''Geeks
#             For
#             Life'''
# print("\nCreating a multiline String: ")
# print(String1)


def get_length(s):
    count = 0
    for c in s:
        count+=1
    return count    

s = "GeeksforGeeks"
# print(get_length(s))

def search_char(s,str):
    
    
    for c in range(len(s)):
        if s[c] == str:
            return c
        
    return -1    

s = "GeeksforGeeks"
ch = 'k'
# print(search_char(s,ch))

# Check if a string is substring of another
'''Given two strings txt and pat, the task is to find if pat is a substring of txt. If yes, return the index of the first occurrence, else return -1.'''

def check_subString(string,checkString):
    n = len(string)
    m = len(checkString)

    for i in range(n - m + 1):
        # print(i)
        j = 0
        while j < m and string[i + j] == checkString[j]:
            j +=1
            print(j)    
        if j == m:
            print('found')
            return i 
    return 'Text not found' 

# Insert a character in String at a Given Position

def insert_position (word,ch,pos):
    res =''
    for i in range(len(word)):
        if i == pos:
            res += ch
        res += word[i]
        if pos > len(word):
            res +=  ch 
    return res           
# Check if two strings are same or not

def checkTwoString(s1,s2):
    if s1 == s2:
        return 'Yes'
    return 'No'
# Concatenation of Two Strings

def twoStringConcat(s1,s2):
    res = s1 + s2
    return res


def reverseStringRec(arr,l,r):
    if l > r:
        return
    arr[l],arr[r] = arr[r],arr[l]
    reverseStringRec(arr, l + 1,r - 1)
def reverseString(s):
    arr = list(s)
    reverseStringRec(arr , 0 , len(arr)-1)

    return ''.join(arr)

if __name__ == "__main__":
    string = 'geeksforgeeks'
    checkString = 'eek'  
    print(check_subString(string,checkString))
    print(insert_position(string,'V',6))
    print(checkTwoString('abc','abc'))  
    print(twoStringConcat('abc','def')) 
    print(reverseString(string)) 