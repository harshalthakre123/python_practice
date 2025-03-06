#variables...

#---Static/class
#---Instance
# ---Local
# 
# 1. Instance variable-- object dependent variables are called instance variable(changes in values and obj changes)

# class Student:
#     def __init__ (self, name, marks):
#         self.x=name   # x and y is called as instance variable which is with self.
#         self.y=marks  # we can access within class by self and externally by object. 
# obj=Student('Harshal', 33) 
# print(obj.x)   #externally calling
# print(obj.y)


class Student2:
    def __init__ (self, name, marks):
        self.x=name   
        self.y=marks  

    def show(self):
        print(self.x)
        print(self.y)
obj= Student2('Harshal', 35)
obj.show() #internally calling

#different object have different address and show different parameters passed and their values.

#self holds the address of the object.

##Declarations:- is we can declare instance variable outside the class
#yes, we can declare instance variable outside from class block.

class ht:
    def disp(self):
        print("disp Method")
    def show(self):
        print("value of x:", self.x)
obj= ht()
obj.x=10
obj.show()






#2. Static/class:-
# the variables which  is not dependent on object or we can say independent is known as static variable or class variable.
# #



