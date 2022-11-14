class User:
    def __init__(self,age):
        self.age=age

user1=User(22)
user2=User(31)
user3=User(11)

minimum_age=[user1.age,user2.age,user3.age]
print(min(minimum_age))