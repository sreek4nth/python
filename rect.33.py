class rect:
    def __init__(self,l,b ):
     self.a1=l
     self.a2=b
    def area(self):
         self.m=self.a1*self.a200
    def peri(self):
             self.n=2*(self.a1+self.a2)
    def disp(self):
                 print("area of rectangle",self.m)
                 print("perimter of rectangle",self.n)
    def compare(self,obj2):
                 if self.m==obj2.m:
                     print("areas are equal")
                 elif self.m > obj2.m:
                     print("area1 is greater than area2")
                 else:
                     print("area2 is greater than area1")
l1=int(input("enter the length1:"))
b1=int(input("enter the breadth1:"))
l2=int(input("enter the length2:"))
b2=int(input("enter the breadth2:"))
obj1=rect(l1,b1)
obj2=rect(l2,b2)
obj1.area()
obj1.peri()
obj2.area()
obj2.peri()
obj1.disp()
obj2.disp()
obj1.compare(obj2)





