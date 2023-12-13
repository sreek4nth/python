class person:
    def __init__(self, fname,lname, id ):
        self.firstname= fname
        self.secondname= lname
        self.id= id
    def printname(self):
        print(self.firstname,self.secondname,self.id)
class student(person):
    def __init__(self,fname,lname,id):
        person.__init__(self,fname,lname,id)
x=person("sreekanth","pradeep",52)
x.printname()

