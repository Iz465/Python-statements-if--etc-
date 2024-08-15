class Person(object):

    # __init__ is the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display(self):
        print(self.name)
        print(self.idnumber)
    
    def details(self):
        print("My name is {}".format(self.name))
        print("My ID number is {}".format(self.idnumber))
    


class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        # Invoking the __init__ of the parent class
        Person.__init__(self,name,idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("My ID number is {}".format(self.idnumber))
        print("My salary is {}".format(self.salary))
        print("My Post is {}".format(self.post))
    
# Creation of an object variable using the init/constructor
a = Employee("John",231,50000,"Software Developer")

# Calling a function of the class person using its instance
a.display()
a.details()
    

        