print(chr(65))
print(ord("B"))

# loops will be clear later on but to clarify
# here we are CREATING (new list of characterS) FROM (list of number).
listOfNo= [1,2,3,4,5,6,7,8,9,10]
listOfCharacters=[]
for no in listOfNo:
    listOfCharacters.append(chr(no+64))

print(listOfCharacters)