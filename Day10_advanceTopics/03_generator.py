def GetPerfectSquare():
    yield 1**2
    yield 2**2
    yield 3**2
    yield 4**2
    yield 5**2

generator = GetPerfectSquare()
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print("Now use for loop to iterate over generator.")
for i in generator:
    print(i)