class User:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    
    def details(self):
        print("Name: ",self.name,",Age: ",self.age,",Email: ",self.email)
        
firstUser=User("Vijay",21,"negivijaysingh21@gmail.com")
print(firstUser.age)
del firstUser.age
print(firstUser.age)
