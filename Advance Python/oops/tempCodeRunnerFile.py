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
obj1=Book("harshal")