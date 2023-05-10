
from unittest import result


class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False


student1 = student("harry", 85)
student2 = student("Janet", 30)

did_pass1 = student1.check_pass_fail()
did_pass2 = student2.check_pass_fail()
# print(did_pass1)
# print(did_pass2)

class Complex:
    def __init__(self, real, imag) -> None:
        self.real = real
        self.imag = imag
    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = complex(real, imag)
        return result

n1 = Complex(5,6)
n2 = Complex(-4,2)
res = n1.add(n2)

print("real: ", res.real)
print("imag: ", res.imag)

class triangle:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

t1 = triangle(3,4,5)
tp = t1.perimeter()
# print(tp)