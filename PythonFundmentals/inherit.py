from firstDemo import a, b
from oopDemo import Calculator

class childImpl(Calculator):
    num2 = 200
    def __init__(self):
       super().__init__(a=10,b=15)

    def getCompletedData(self):
        return self.num + self.num2 + self.sum()
obj = childImpl()
print(obj.getCompletedData())