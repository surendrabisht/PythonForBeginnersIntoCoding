value=5
print(f"your luck no is {value} and you have lost it. ")
print("your luck no is {} and you have lost it. ".format(value))


no=int(input("Enter the no:"))
i=1
while i<=10:
    print(f" {no} X {i} = {no*i}")
    i+=1

i=i+16

if i>5:
 print("yes1")
if i>10:
 print("yes2")
 
if i>30:
 print("yes3")
elif i>35:
 print("yes5")   
else:
 print("yes4")

print(" Program exit")