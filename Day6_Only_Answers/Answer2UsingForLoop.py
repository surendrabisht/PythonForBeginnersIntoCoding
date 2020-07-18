fees = int(input("Enter the amount: "))
noOfNotesReq=0
messageToShow=""
denominations=(500,100,50,20,10,5,2,1)

for note in denominations:
    noOfNotesReq+=fees//note
    if (fees//note)>0:
        messageToShow+= f"\n {note} notes: "+str(fees//note)
    fees=fees%note

print(noOfNotesReq)
print(messageToShow)
