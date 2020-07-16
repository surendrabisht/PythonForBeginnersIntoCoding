def new_decorator(original_func):
    def wrapper_func(expression):
        print("******************************")
        print("Result of input: ",expression," is ",end=": ")
        original_func(expression)
        print("******************************")
    return wrapper_func

def func_need_to_be_decorated(expression):
    print(eval(expression))

inputExpression=input("Enter the maths expression to get result: ")
print("")
func_need_to_be_decorated(inputExpression)
print("")
decorated_func= new_decorator(func_need_to_be_decorated)
decorated_func(inputExpression)

@new_decorator
def powerOf2(no):
    print(no**2)


powerOf2(9)
