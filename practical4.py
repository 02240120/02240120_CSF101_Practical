#array methods
'''
blackpink = ["Jennie", "Lisa", "Jisoo", "Rosie" 1290]
blackpink.append("Jigme")
blackpink.pop("Lisa")
blackpink.remove(1290)
blackpink.insert(2"Jigme")

blackpink = ["Jennie", "Lisa", "Jisoo", "Rosie"]
Newstack =[]
Array_length = len(blackpink)

For index in range(Array_length): 
    temporaryPopholder = blackpink.pop
    Newstack.append(temporaryPopholder)

Print(blackpink)
Print(Newstack)


def multiply(x:int,y:int)
    
def multiplyfunction (firstelement:int,secondelement:int) -> int:
    product = firstelement * secondelement
    return "hehe"

firstnumber = 12
secondnumber = 15

print(multiplyfunction(firstnumber, secondnumber))



def squarefunction(firstelement:int,) -> int:
    product = firstelement**2
    return product

firstnumber = 8

print(squarefunction(firstnumber))'''



#sets and tuples
#set- unique elements (won't save dupes; only keeps one copy)
#tuples - immutable(once you put something in the tuple, you cannot remove it)

new_tuple = (11,12,13,14, "sonam")

print(new_tuple)
print(len(new_tuple))

#if question asks to find how many duplicates are there in an array

array ={11,12,14,11,15,15,18}
sampleset = set(array)


diff = len(array) - len(sampleset)

print("there are", diff, "duplicates")