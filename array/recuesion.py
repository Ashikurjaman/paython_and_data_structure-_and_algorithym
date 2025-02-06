# Sum of Natural Numbers

def sumOfNaturalNumber(n):
    if n == 0:
        return 1
    return n * sumOfNaturalNumber(n-1)

n = 5
print(sumOfNaturalNumber(n))