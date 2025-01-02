exp = [2200,2350,2600,2130,2190]

print(f"In Feb, how many dollars you spent extra compare to January",exp[1]-exp[0])

print(f"Find out your total expense in first quarter (first three months) of the year.",exp[0]+exp[1]+exp[2])

print("Did I spent 2000$ in any month? ", 2000 in exp)

exp.append(1980)
print(exp)   

exp[3]=exp[3]-200
print("Expenses at the end of June:",exp)

heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))
heros.append('black panther')
print(heros)

heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
heros[1:3]=['doctor strange']
print(heros)
heros.sort()
print(heros)

input_number=int(input())
list_nub=[]
for i in range(1,input_number):
    if i%2 !=0:
        list_nub.append(i)
print(list_nub)        


max = int(input("Enter max number: "))

odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)