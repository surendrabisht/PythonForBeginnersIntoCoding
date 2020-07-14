x = 'Hi'
def read_x():
    global x
    x="world"
    print(x)

read_x()
print(x)