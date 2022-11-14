class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def details(self):
        print("Name: ",self.name,",age: ",self.age)

user1=User("Vijay",21)
user2=User("Nikhil",24)
user1.details()
user2.details()
        