class Laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
    def showConfig(self):
        print(f"Brand = {self.brand}\nRam = {self.ram}\nCpu = {self.cpu}\nHdd = {self.hdd}")
    
laptop1=Laptop("Apple","8Gb","ios","1Tb")
laptop2=Laptop("Dell","8Gb","intelcorei3","1Tb")
laptop3=Laptop("Hp","4Gb","Ryzen9","1Tb")
list=[laptop1.ram,laptop2.ram,laptop3.ram]
print(sorted(list))