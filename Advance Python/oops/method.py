# methods
    # ----instance method
    # ----class method @classmethod
    # ----static @ststicmethod
# @ is called decorator


#=================================================================================================

# 1.Instance method:-  the method in which first parameter is self is instance method.

# class Student:

#     def first(self):
#         print("This is from first")

#     def second(self):
#         obj1= Student()   #we can create obj for any class in any other class.
#         obj1.first()
#         # Student.first(self)
# obj=Student()
# obj.first()
# obj.second()

#==================================================================================================

#2.Class method:- it is used to change the static/class variable.
# use:- @classmethod

class Book:
    price=100
    total_pages=300

    def __init__(self, st_name):
        self.x=st_name
        print(self.x, Book.price, Book.total_pages)
#cls is class used to target class and self is used to target object, we can use any variable instead of cls.
    @classmethod   #to modify Static/class variable we use @classmethod. 
    def update(cls, p, q):
        cls.price=p
        cls.total_pages=q

obj1=Book('Neeraj')
obj2=Book('Harshal')

Book.update(150, 450)
obj1=Book('Nikhil')


# self is related to object and cls is related to class and in static method we use nothing.


#===============================================================================================================


#3.Static method