# classes are bluePrint or prototype
# sum, multiplication, addition, constant
# methods, class variables, instance variables, constructor
#objects for your classes
class Calculator:
    num = 100 # class variables, it will be constant instead of the numbers of objects you will create

    def __init__(self,a,b):
        self.number1 = a
        self.number2 = b
        print("I am called default constructor")

    def getData(self):
        print("I am now executing as method in class")

    def sum(self):
        return self.number1 + self.number2
        # print("The sum is {}".format(self.number1 + self.number2))

# creating an object syntax in python
obj = Calculator(2,3)
obj.getData()
print(obj.sum())

