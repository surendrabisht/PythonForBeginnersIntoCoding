startLimit = int(input("Enter the start limit: "))
endLimit = int(input("Enter the end limit: "))
gap = int(input("Enter the gap: "))
while startLimit<=endLimit:
    print(startLimit,end=" ")
    startLimit=startLimit+gap
