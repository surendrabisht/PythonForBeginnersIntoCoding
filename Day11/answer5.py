# todo: implement logic to handle the case for -ve no.s
def AbsoluteNo(no):
    if no<0:
        no*=-1
    return no

print(AbsoluteNo(int(input(" Enter the no: "))))
