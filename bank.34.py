class bank:
    def __init__(self,a,n,t,b):
        self.ac=a
        self.name=n
        self.type=t
        self.bal=b
    def depo(self,a1):
         self.bal+=a1
         print("balance:",self.bal)
    def withdraw(self,a2):
         if self.bal<a2:
             print("invalid")
         else:
             self.bal-=a2
             print("balance:",self.bal)
    def disp(self):
        print("Acc No:",self.ac)
        print("name:",self.name)
        print("Acc Type:",self.type)
        print("Acc balance:",self.bal)
a=int(input("enter acc no:"))
n=input("enter name:")
t=input("enter acc type:")
b=int(input("Enter balance:"))
obj1=bank(a,n,t,b)
obj1.disp()
a1=int(input("Enter the amount to deposite:"))
obj1.depo(a1)
a2=int(input("enter the amount to widthdraw:"))
obj1.withdraw(a2)