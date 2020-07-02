
x=int(input("Enter the unit to find your electricity rent: "))
expense=0

if x<=50:
    expense  =x * 0.5
    print(f" expense till now for {x} is {expense} ")
else:
    expense=50*0.5
    x=x-50
    print(f" expense till now for 50 is {expense} ")
    if x<=100:
        expense=expense + x *0.75
        print(f" expense till now for {x} is {expense} ")
    else:
        expense=expense + 100 * 0.75
        x=x-100
        print(f" expense till now for 100 is {expense} ")
        if x <=100:  
            expense=expense+ x * 1.2
            print(f" expense till now for {x} is {expense} ")
        else:
            expense=expense + 100 * 1.2
            x=x-100;   
            print(f" expense till now for 100 is {expense} ")       
            expense= expense + x *1.5
            print(f" expense till now for {x} is {expense} ")
expense = 1.20 * expense

print("Expense for the month is {}".format(expense))