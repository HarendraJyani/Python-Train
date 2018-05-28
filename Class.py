import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        r1 = self.real
        i1 = self.imaginary
        r2 = no.real
        i2 = no.imaginary
        resultR = r1 + r2
        resultI = i1 + i2
        result = Complex(resultR,resultI)
        return result
        
    def __sub__(self, no):
        r1 = self.real
        i1 = self.imaginary
        r2 = no.real
        i2 = no.imaginary
        resultR = r1 - r2
        resultI = i1 - i2
        result = Complex(resultR,resultI)
        return result
        
    def __mul__(self, no):
        r1 = self.real
        i1 = self.imaginary
        r2 = no.real
        i2 = no.imaginary
        resultR = r1*r2 + (-1)*i1*i2
        resultI = r1*i2 + i1*r2
        result = Complex(resultR,resultI)
        return result

    def __truediv__(self, no):
        r1 = self.real
        i1 = self.imaginary
        r2 = no.real
        i2 = no.imaginary
        resultR = float(float(r1*r2+i1*i2)/float(r2*r2+i2*i2))
        resultI = float(float((-1)*r1*i2 + i1*r2)/float(r2*r2 + i2*i2))
        result = Complex(resultR,resultI)
        return result

    def mod(self):
        r1 = self.real
        i1 = self.imaginary
        sqr = math.sqrt(r1*r1 + i1*i1)
        result = Complex(sqr,0)
        return result

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
    
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
