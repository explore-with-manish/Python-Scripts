class Example:
    _name = "Manish"

    @staticmethod
    def testMethod1():
        return Example._name

    @classmethod
    def testMethod2(cname):
        return cname._name

print(Example.testMethod1())
print(Example.testMethod2())        # testMethod2(Example)


# @staticmethod function is nothing more than a function defined inside a class. 
# It is callable without instantiating the class first. It’s definition is immutable via inheritance.

# @classmethod function also callable without instantiating the class, 
# but its definition follows Sub class, not Parent class, via inheritance