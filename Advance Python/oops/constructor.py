#constructor 

class Student:
    def __init__(self):
        print("Constructor called")
        
    def __init__(self):
        print("Constructor x called") #it is called function overloading.

# obj= student #in this case it create obj and gives memory address.(inbuild constructor called)
obj=Student() #o/p Constructor called (parenthesis is necessary for external constructor).

# class name starts with capital letter because it cannot differentiate between functions and class.

# we can call constructor externally by using __init__()

obj.__init__()

#how much constructor we can create in a class? ans-- we can create n no. of constructors but it always call the last constructor which is not override.

# Class without constructor is possible 
# We cannot create the object of any class without calling any inbuild or external constructor. 
# Parenthesis() is responsible for calling external constructor. 
