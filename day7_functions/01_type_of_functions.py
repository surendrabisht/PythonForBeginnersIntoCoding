def sum(a,b):
    return a+b

def GetDate():
    return '2020-07-06'

def GetSquareOfNo(no):
    return f'Square of  {no}  is {no*no}'

def A_PlusB_Square(a,b):
    return a*a +b*b + 2*a*b

def printHurrey():
    print("Hurrey")


printHurrey()
x=int(input("Enter the value : "))
y= GetSquareOfNo(x)
print(y)

printHurrey()

z=A_PlusB_Square(20,5)
print(z)

printHurrey()

x=GetDate()
print(x)

printHurrey()

c=sum(23,56)
print(c)