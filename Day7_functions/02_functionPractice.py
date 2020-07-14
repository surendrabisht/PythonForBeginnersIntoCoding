def GetCubeOfNo(no):
    return f'Cube of {no} is {no**3}'

# multiple function calls in one line where result of each function 
# is passed as argument to another function.
print( GetCubeOfNo( int( input("Enter the no: ") ) ) )
