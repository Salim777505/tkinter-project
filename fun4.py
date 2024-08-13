class shape:
    def area(self):
        pass
class square(shape):
    def __init__(self,zool):
        self.zool=zool
    def area(self):
        
        return f'{self.zool **2}'

class tringle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return f'{self.base * self.height * 0.5}'

s=square(4)
print(s)
