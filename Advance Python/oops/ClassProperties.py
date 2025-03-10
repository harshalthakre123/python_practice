#Class Properties
    #Data-Protection
        # a-Abstraction
        # b-Encapsulation
    #Code-Resuable    
        # c-Inheritance
        # d-Polymorphism


# Inheritance:-
#   --Parent child relationship is called as inheritance
 
# Types of inheritance:

# --------------------------------------------------------------------------------------------------------------
#   -1.Single Level Inheritance

#           [parent]
#               |
#            [child]

# class parent:
#     def bank(self):
#         print("This is from c class")
# class child(parent): 
#     def car(self):
#         print("car from child")
# obj=child()
# obj.bank()
# print(obj.x)
# obj.car()


# ---------------------------------------------------------------------------------------------------------------
#   -2.Multiple Inheritance(More than 1 parent of child class)
#      
#      [Parent] [parent]
#            |    |
#            [child]
# 

# class parent1:
#     x=10
#     def home(self):
#         print("home from parent")
# class parent2:
#     def bank(self):
#         print("This is from c class")
# class child(parent2, parent1):   # left parent is on high priority which is known as MRO(method resolution order) in which depth first search algorithm work which works left to right only. 
#     def car(self):
#         print("car from child")
# obj=child()
# obj.home()
# print(obj.x)
# obj.car()
# obj.bank()


# #MRO-logic========================================================

# class parent1:
#     x=10
#     def bank(self):
#         print("home from parent")
# class parent2:
#     def bank(self):
#         print("This is from c class")
# class child(parent2, parent1):   # left parent is on high priority which is known as MRO(Method Resolution Order) in which depth first search algorithm work which search left to right only. 
#     def car(self):
#         print("car from child")
# obj=child()
# obj.bank()




#Method Overriding============================================================

# class parent:
#     def home(self):
#         print("this is from parent class")

# class child(parent):
#     def home(self):
#         print("this is from child class")
#         super().home()   #super() is used to call overrided method from parent class directly
# obj=child()
# obj.home()
# #



# -----------------------------------------------------------------------------------------------------------
#   -3.Multilevel Inheritance
#            
#           [Parent]
#              |
#           [Parent] 
#              |      
#           [child]


# class Grandparent:
#     def home(self):
#         print("from Grandparent")

# class Parent(Grandparent):
#     def car(self):
#         print("from Parent")

# class Child(Parent):
#     def car(self):
#         print("from Child")
#         super().car()
# obj=Child()
# obj.home()
# obj.car()


# ------------------------------------------------------------
class Grandparent:
    def car(self):
        print("from Grandparent")

class Parent(Grandparent):
    def car(self):
        print("from Parent")
        
class Child(Parent):
    def car(self):
        print("from Child")
        super(Parent, self).car()
obj=Child()
# obj.home()
obj.car()



#--------------------------------------------------------------------------------------------------------------
#   -4.Heirarchical Inheritance
#           [Parent]
#          |        |
#     [child]     [Child]








#--------------------------------------------------------------------------------------------------------------
#   -5.Hybrid Inheritance#