userName="Sonu"
pwd = "asdf"
inputUn = input("Enter Name  : ")
inputPwd = input("Enter Pwd : ")

if inputUn.lower()=="admin":
   print("welcome admin . Login Succesful .")

else:
    if inputUn == userName and inputPwd==pwd :
        print("welcome "+userName+" .  Login Succesful .")
    elif inputUn == userName or inputPwd==pwd :
        print("Either pwd or username is wrong .")
    else:
        print("Wrong username & pwd entered. ");

print("Pogram exit.");

