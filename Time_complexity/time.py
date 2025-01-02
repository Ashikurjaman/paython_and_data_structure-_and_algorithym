# import time
# start = time.time()
# count = 0
# i =1
# while i<101:
#     print(i)
#     count +=1
#     i+=1
# # for i in range(1,101):
# #     count +=1
    

# print(count)    
# print(time.time()-start)    

# O(n) big o notation

def fact_check(n):
    answer = 1
    while n>1:
        answer*=n
        n-=1
    return answer    
print(fact_check(5))        

L =[1,2,3,4,5]

for i in range(0,len(L)//2):
    others = len(L) -i -1
    temp = L[i]
    L[i] =L[others]
    L[others] =temp
print(L)    
