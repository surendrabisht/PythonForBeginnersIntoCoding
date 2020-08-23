class Bathroom:
    #cannot be accessed outside the class normally. #private can be used as obj._Bathroom__noOfTaps
    __noOfTaps=2
    def __init__(self):
        self.Type="IndianStyle"
    
    @classmethod
    def GetWesternStyle(cls):
        westernStyle= Bathroom()
        westernStyle.Type="WesternStyle"
        return westernStyle

    # used as utility method. Has nothing to do with class attributes and states.    
    @staticmethod
    def Description():
        print(f" Bathroom object in system is mapped to Bathroom entity.")
    
    def Show(self):
        return f"Bathroom type: {self.Type} and taps available are {self.__noOfTaps}"
    
    def __str__(self):
        return f"Bathroom type: {self.Type} and taps available are {self.__noOfTaps}"


if __name__ == "__main__":
    bathroom = Bathroom()
    print(bathroom.Show())
    Bathroom.Description()



    