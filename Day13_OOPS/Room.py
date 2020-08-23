class Room:
    __totalChairs=4
    def __init__(self,roomNo:str) ->str :
        self.roomNo=roomNo
        self.__totalChairs=2

    @classmethod
    def GetDefaultRoom(cls):
        room1= Room("DrawingRoom")
        room1.__totalChairs=9
        return room1

    def printRoomno(self):
        print(self.roomNo)

    def __str__(self):
        return f"Rooom Type: {self.roomNo}  with total chairs {self.__totalChairs}"  


if __name__ == "__main__":
    room= Room("LH-202")
    room.printRoomno()
    print(room)
    room=Room.GetDefaultRoom()
    print(room)



