import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width = None):
        if width:
            n = length * width
            return n
        else:
            n = math.pi * length ** 2
            n = round(n, 2)
            return n
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
