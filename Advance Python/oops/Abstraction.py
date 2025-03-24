# Abstraction

from abc import ABC,  abstractmethod

# class A(ABC):
#     def new(self):
#         print("80%")
    
#     @abstractmethod
#     def new1(self):
#         pass

# class B(A):
#     def first(self):
#         print("20%")

# obj=B()
# obj.new()



class Bank(ABC):
    def reg(self):
        print("Registration Page")
    
    def logout(self):
        print("logout_page")

    @abstractmethod
    def authentication(self):
        pass

    def Dashboard(self):
        print("From Dashboard")

class Webpage(Bank):
    def login(self, id, passw1):
        self.id= id
        self.passw1= passw1

    def authentication(self):
        print("Authentication Done")

    # def Dashboard(self):
    #     print("From Dashboard")


# class MobApp(Bank):
#     def login(self, userid, password):
#         self.id= id
#         self.passw= passw
#     def Dashboard(self):
#         print("From Dashboard")


obj=Webpage()
obj.login(101, 123)
obj.Dashboard()

