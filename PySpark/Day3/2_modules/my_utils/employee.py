class Employee:
    def __init__(self, id=0, name="NA", desig="NA", sal=0):
        self._id=id
        self._name=name
        self._designation=desig
        self._salary=sal

    def getId(self):
        return self._id
    
    def getName(self):
        return self._name

    def getDesignation(self):
        return self._designation
    
    @property
    def Salary(self):
        return self._salary
    
    @Salary.setter
    def Salary(self, value):
        if(value<10000):
            raise ValueError("I will not work less than 10000/hour")
        self._salary = value