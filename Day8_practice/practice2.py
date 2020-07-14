# Small if else program to just simulating 
# the behaviour of window buttons- min,max and close buttons on any window.

windowSize ='default'  # min ,max ,default
while True:
    buttonClicked= input("Button :")
    if buttonClicked=='max':
        if windowSize=='default': 
           windowSize= "max"
        else:
           windowSize='default'
    elif buttonClicked =='close':
        break
    elif buttonClicked=='min':
         windowSize='minimize'
    print("current window state: ",windowSize)

print("Program Terminated.")
     

       
    