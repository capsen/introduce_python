class Employee:
    def __init__(self, name, project, salary):
        self.name = name
        self._project = project
        self.__salary = salary

    def getmySalary(self):
        return self.__salary

e1 = Employee("Tom", "AI", 300000)
print(e1.name)
print(e1._project)
print(e1.getmySalary())