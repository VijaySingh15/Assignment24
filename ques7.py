class Laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
        
    def showConfig(self):
        print("Brand : ",self.brand,"\nRam : ",self.ram,"\nCpu : ",self.cpu,"\nHdd : ",self.hdd)

details=Laptop("Apple","8GB","ios","1TB")
details.showConfig()