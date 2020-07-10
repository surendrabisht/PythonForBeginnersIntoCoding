while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break
   elif user_input == "add":
      i= int( input("first no: "))
      j= int(input("second no: "))
      print(i+j)
   elif user_input == "subtract":      
      i= int( input("first no: "))
      j= int(input("second no: "))
      print(i-j)
   elif user_input == "multiply":
      i= int( input("first no: "))
      j= int(input("second no: "))
      print(i*j)
   elif user_input == "divide":      
      i= int( input("first no: "))
      j= int(input("second no: "))
      print(i/j)
   else:
      print("Unknown input")