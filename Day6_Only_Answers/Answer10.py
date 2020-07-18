A=int(input("enter your percentage in \"A\""))  #Variable
B=int(input("enter your percantage in \"B\"")) #Variable
if (A>=55) and (B>=45):
    print("Pass 1 ")
elif(A>=45) and (A<=55) and (B>=55):
    print ("pass 2")
elif(B<45) and (A>=65):
    print ("you are allwed to reappear")
else:
    print("fail game over")