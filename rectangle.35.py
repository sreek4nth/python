class rectangle:
    def __init__(self,l,b):
        self._l1=l
        self._b1=b
    def area(self):
        area1=self._l1 * self._b1
        return area1
    def __lt__(self,obj):
        if(self.area()<obj.area()):
            return"the area of rectangle1 is less than rectangle2"
        else:
            return"the area of rectangle2 is less than rectangle1"
print("RECTANGLE 1")
l=int(input("enter the length of rectangle1:"))
b=int (input("enter the breadth of rectangle1:"))
obj1=rectangle(l,b)
print("the area is:")
print(obj1.area())
print("RECTANGLE 2")
l=int(input("enter the length of rectangle 2:"))
b=int(input("enter the breadth of rectngle 2:"))
obj2=rectangle(l,b)
print("the area is:")
print(obj2.area())
print("now comparing the rectangles")
print(obj1 < obj2)


