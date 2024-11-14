class Example:
    _name = "Manish"

    @staticmethod
    def testMethod1():
        return Example._name
    
    @classmethod
    def testMethod2(cls):
        return cls._name
    

print(Example.testMethod1())
print(Example.testMethod2()) 