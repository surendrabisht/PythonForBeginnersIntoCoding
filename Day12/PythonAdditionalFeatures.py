# 1. The else statement is most commonly used along with the if statement,
#but it can also follow a for or while loop, which gives it a different meaning.
#With the for or while loop, the code within it is called if the loop finishes 
# normally (when a break statement does not cause an exit from the loop).

for i in range(10):
   if i == 999:
      break
else:
   print("Unbroken 1")


#2. The else statement can also be used with try/except statements.
#In this case, the code within it is only executed if no error occurs in the try statement.

#3. Ternary Operator
a = 7
b = 1 if a >= 5 else 42


#4.this code will run only  when the script is run. if this file is imported as module, them
# the cde written under this check will not run.
# _name_ will be _main_ only when the program is executed as script.
if __name__=="__main__":
    print("This is a script code. will not run on this module import.")

#5. The module matplotlib allows you to create graphs based on data in Python.
#6.The module NumPy allows for the use of multidimensional arrays that are much faster 
# than the native Python solution of nested lists
#7. For scraping data from websites, the library BeautifulSoup
