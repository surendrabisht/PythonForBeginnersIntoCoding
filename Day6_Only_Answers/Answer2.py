fees = int(input("Enter the amount: "))

#listOfDenominations =[500,100,50,20,10,5,2,1]
noOfNotesReq=0
messageToShow=""
if (fees>=500):
    noOfNotesReq+=fees//500
    messageToShow+= " 500 notes: "+str(fees//500)
    fees=fees%500 

if (fees>=100):
    noOfNotesReq+= fees//100
    messageToShow+= ", 100 notes: "+str(fees//100)
    fees =fees%100 
if (fees>=50):
    noOfNotesReq+= fees//50
    messageToShow+= ", 50 notes: "+str(fees//50)
    fees =fees%50
if (fees>=20):
    noOfNotesReq+= fees//20
    messageToShow+= ", 20 notes: "+str(fees//20)
    fees =fees%20
if (fees>=10):
    noOfNotesReq+= fees//10
    messageToShow+= ", 10 notes: "+str(fees//10)
    fees =fees%10
if (fees>=5):
    noOfNotesReq+= fees//5
    messageToShow+= ", 5 notes: "+str(fees//5)
    fees =fees%5
if (fees>=2):
    noOfNotesReq+= fees//2
    messageToShow+= ", 2 notes: "+str(fees//2)
    fees =fees%2
if (fees>=1):
    noOfNotesReq+= fees//1
    messageToShow+= ", 1 notes: "+str(fees//1)
    
print(noOfNotesReq)
print(messageToShow)
    


 

#noOfNotesReq = x+y #+......+noof1notes

