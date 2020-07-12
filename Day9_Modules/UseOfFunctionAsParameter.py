def CubeOfNo(no):
    return no**3

def ReverseNo(no):
    string= str(no)
    return int(string[::-1])

def ConvertToBinary(no):
    binary=''
    while no!=0:
        binary=binary+str(no%2)
        no=no//2
    return int(binary[::-1])
    


def ManipulateListElements(logicToAppy,data):
    i=0
    while i<len(data):
        data[i]=logicToAppy(data[i])
        i+=1

listOfNo =[1,12,3,15,5,6]
print(listOfNo)
#ManipulateListElements(CubeOfNo,listOfNo)    
#ManipulateListElements(ReverseNo,listOfNo) 
ManipulateListElements(ConvertToBinary,listOfNo) 
print(listOfNo)  



