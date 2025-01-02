def linear_search (L,x):
    # n=len(L)
    # i = 0
    # while i < n:
    #     if L[i] == x:
    #         return i
    #     i +=1
    # i = -1
    # return i    
     
      n=len(L)

      for i in range(n):
            if L[i] == x:
                return i
      return -1
print (linear_search([1,2,3,4,5,6,7],5))


def star(n):
     for i in range(n+1):
          print("*" * i)

star(5)

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 == 0:
        print('Weird')
    elif 2<= n <=5:
        print("Not Weird")    
    elif 6<=n <=20:
        print("Weird")    
    elif n > 20:
        print("Not Weird")  