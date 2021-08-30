import inspect

def log(function):
    def wrapper(*args,**kwargs):
        bound_args = inspect.signature(function).bind(*args, **kwargs)
        bound_args.apply_defaults()
        print(f"function call -> {function.__name__}({dict(bound_args.arguments)}); ")
        # function call
        returned_value= function(*args,**kwargs)
        
        print(f"function returned -> {returned_value} ")
        return returned_value
    return wrapper

@log
def sum(a,b):
    return a+b

@log
def sum_three(a,b,d,c=34):
    '''
    yo yo
    '''
    return a+b+c

@log
def GetDate():
    return '2020-07-06'
@log
def GetSquareOfNo(no):
    return f'Square of  {no}  is {no*no}'

@log
def A_PlusB_Square(a,b):
    '''
    sddsdsdasdsadaasdasdas
    '''
    print("asd")
    return a*a +b*b + 2*a*b

print(sum(4,5))
print(GetDate())
print(sum_three(4,5,{"h":"sdf"}))



