# #variables in function...

# #---Static/class
# #---Instance
# # ---Local
# # 
# # 1. Instance variable-- object dependent variables are called instance variable(changes in values and obj changes)

# # class Student:
# #     def __init__ (self, name, marks):
# #         self.x=name   # x and y is called as instance variable which is with self.
# #         self.y=marks  # we can access within class by self and externally by object. 
# # obj=Student('Harshal', 33) 
# # print(obj.x)   #externally calling
# # print(obj.y)


# class Student2:
#     def __init__ (self, name, marks):
#         self.x=name   
#         self.y=marks  

#     def show(self):
#         print(self.x)
#         print(self.y)
# obj= Student2('Harshal', 35)
# obj.show() #internally calling

# #different object have different address and show different parameters passed and their values.

# #self holds the address of the object.

# ##Declarations:- is we can declare instance variable outside the class
# #yes, we can declare instance variable outside from class block.

# class ht:
#     def disp(self):
#         print("disp Method")
#     def show(self):
#         print("value of x:", self.x)
# obj= ht()
# obj.x=10
# obj.show()






# #2. Static/class:-
# # the variables which  is not dependent on object or we can say independent is known as static variable or class variable.
# #
# class Student2:
#     school='SHSS'
#     city= 'Bhopal'

#     def __init__(self, name, roll):
#         self.x= name 
#         self.y= roll

#     def show(self):
#         print(self.x, self.y)
#         print(Student2.school)
#         print(Student2.city)

# #obj=Student2;
# obj1=Student2('Harshal' , 101)
# obj1.show()
# obj2=Student2('Harsh', 100)
# obj2.show()


#declarations of static variable:-
# 1.Inside class
#       a--outside method
#       b--inside instance method
#       c--inside constructor

# 2. Outside class
# syntax
# Class_name.variable=value_assigned


# class School:
#     school_name="SPPS" #outside method

#     def __init__(self, name, roll):
#         self.x= name
#         self.y= roll
#         School.city="Bhopal"

#     def show(self):
#         School.S_code= 123

#     def display(self):
#         print(School.S_code)
#         print(School.city)
#         print(School.school_name)
#         print(School.principal)

# School.principal= "Nikhil"
# obj=School("Harshal", 84)
# obj.show()
# obj.display()


##we can call the static function externally with or without object(By class) but we only call it by class name because it is not object dependent.
# print(school.school_name)
# #








#3. Local Variable---- the variable which is declared inside the method without using self or classname. is known as local variable and is only accessable in a block only.
#ex:-- p=100 (inside method)