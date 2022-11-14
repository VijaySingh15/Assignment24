class School:
    schoolName="BBL Public School"
    def __init__(self,name,roll,standard):
        self.name=name
        self.roll=roll
        self.standard=standard

s1=School("Vijay",53,"X")
print(s1.schoolName,s1.name,s1.roll,sep="\n")