class Book:
    def __init__ (self):
        print("Constructor Called")

    @staticmethod
    def welcome():
        print("Welcome to my page")

    @staticmethod
    def thanks():
        print("Thanks for visit")
obj=Book()