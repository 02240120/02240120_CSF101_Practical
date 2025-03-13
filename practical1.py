'''name =("Jigme")
print(name)
small = True
print(small)

a = 5
b = 7
c = a*b
print(c)

Dorji = 23
Tobgay = 20
if Dorji>Tobgay:

    print("Dorji is older than Tobgay")
else:
    print("Kezang is older than Dorji")'''

#Exercise_1

first_list = [0,1,2,3,4,5,6,7,8,9]
inverse_list = []

length_of_first_list = len(first_list)
index = 0

#Hint, use a while loop to loop throught first list from the last index
while index < length_of_first_list:
  inverse_list.append(first_list.pop())
  index += 1

print(first_list)
print(inverse_list)


