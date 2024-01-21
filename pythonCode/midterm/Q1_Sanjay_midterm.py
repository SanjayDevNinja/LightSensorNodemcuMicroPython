class Employee:
    __id = 100

    def __init__(self,name,programme='Scientific Programme',department='Software') -> None:
        self.__id = Employee.__id
        Employee.__id +=1

        self.__name = name
        self.__programme = programme
        self.__department = department

    @property              #another property
    def id(self):
        return self.__id

    @id.setter             #the corresponding setter
    def id(self, id):
        self.__id = id

    @property              #another property
    def name(self):
        return self.__name

    @name.setter             #the corresponding setter
    def name(self, name):
        self.__name = name    

    def __str__(self) -> str:
        return   f''' 
        Id: {self.__id}
        Name: {self.__name}
        Programme: {self.__programme}
        Department: {self.__department}''' 

#Display 3 Employees
Emp1 = Employee('Sanjay','Operations Programme','CEO')
Emp2 = Employee('Max')
Emp3 = Employee('Jack','Research Programme','Laboratory')

Emp2.id = 999

print(Emp1)
print(Emp2)
print(Emp3)