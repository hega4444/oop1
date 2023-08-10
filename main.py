class Mesias():
    #general definition of Mesias class
    def __init__(self) -> None:
        #attributes of Mesias
        self.holy_message = "Wisdom has a price. Insert a coin."
        self.followers = 1
    
    def preech(self):
        #object method for Mesias
        print(self.holy_message)

class Jesus(Mesias):
    def __init__(self) -> None:
        super().__init__()
        self.holy_message = "I need 12 people to start a cult, wanna join?."

class Buddha(Mesias):
    def __init__(self) -> None:
        super().__init__()
        self.holy_message = "Try not to be an moron."


great_mesias = Mesias()
great_mesias.preech()

another_mesias = Jesus()
another_mesias.preech()

last_mesias = Buddha()
last_mesias.preech()


