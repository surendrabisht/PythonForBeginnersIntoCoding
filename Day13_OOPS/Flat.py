#from .Bathroom import Bathroom
#from .Room import Room

from Bathroom import Bathroom
from Room import Room

class Flat:
    __bathrooms=[]
    __rooms=[]

    def __init__(self):
        bathroom= Bathroom()
        self.__bathrooms.append(bathroom)
        room=Room("BedRoom")
        self.__rooms.append(room)

        
    

    @classmethod
    def get2BHKFlat(cls):
      twoBHK= Flat()
      twoBHK.__bathrooms.append(Bathroom.GetWesternStyle())
      twoBHK.__rooms.append(Room.GetDefaultRoom())
      return twoBHK

    def __str__(self):
        flatDescription="Rooms:\n"
        for room in self.__rooms:
          flatDescription+=room.__str__()+" ; "
        flatDescription+="\nBathrooms:\n"
        for bathroom in self.__bathrooms:
          flatDescription+=bathroom.__str__()+" ; "
        
        return flatDescription


oneRoomFlat=Flat()
print(oneRoomFlat)
print("-------------------------")
twobhk= Flat.get2BHKFlat()
print(twobhk)