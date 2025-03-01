from firstDemo import a, b
from oopDemo import Calculator

class childImpl(Calculator):
    num2 = 200
    def __init__(self):
        Calculator.__init__(self,10,20)


    def getCompletedData(self):
        return self.num + self.num2 + self.sum()
obj = childImpl()
print(obj.getCompletedData())