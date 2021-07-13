# Cleate Python Classes Methods
class Doctors:
    """This is all about doctors"""
    def __init__(self,name,subject,disease,health):
        self.name = name
        self.subject = subject
        self.disease = disease
        self.health = health

    def intro(self):
        print(f"My name is {self.name}. I persued {self.subject}. Im very hapy")
    def __str__(self):
        return
        pass


    def func(self):
        print("this is public")

    def __func(self):
        print("this is private")

class Dentist(Doctors):
    """inherits Doctors atttr"""
    def __init__(self,name,subject,disease,health,cid):
        super().__init__(name,subject,disease,health)
        self.id = cid

p1 = Doctors("Fancy","biology","insomnia","bad")
print("below prints p1")
print(p1)
print("when special clss is called on an object")
print(p1.__str__())
print("below prints p2'disease")
p2 = Doctors("peter","chemistry","none","good")
print(p2.disease)
print("below prints p2")
print(p2)
print("below calls public func 'intro' on p2")
# calling function  on an instance of a class
print(p2.intro())

print("below calls public func 'func' on p2")
print(p2.func())
print("1 below calls private func '__func' on p2")
print(p2._Doctors__func())
#print("2 below calls private func '__func' on p2")
#print(p2.__func())

# subclass
d1 = Dentist("Dennis","maths","typhoid","baad",23)

print(f"{d1}\n")
print(f"{d1.subject}\n")
print(f"{d1.intro()}\n")
print("below calls public class from main class on an instancs of subclass")
print(d1.func())

print("\nbelow tries to call private class from main class on an instance of subclass")
#print(d1.__func())

print("\nbelow is correct way to call private class from main class on an instance of subclass")

print(d1._Doctors__func())
