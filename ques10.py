class Employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
    
    def fields(self):
        print(f"Employee id : {self.empid}\nName : {self.name}\nSalary : {self.salary}")

e1=Employee("48393","Vijay",100000)
e2=Employee("27282","Sachin",90000)
e1.fields()
e2.fields()
