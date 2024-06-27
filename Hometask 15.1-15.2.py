# #Hometask 15.1
# import math
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.get_square() == other.get_square()
#         return False
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             total_area = self.get_square() + other.get_square()
#             width = self.width
#             height = total_area / width
#             return Rectangle(width, height)
#         return NotImplemented
#
#     def __mul__(self, n):
#         if isinstance(n, (int, float)):
#             new_area = self.get_square() * n
#             width = self.width
#             height = new_area / width
#             return Rectangle(width, height)
#         return NotImplemented
#
#     def __str__(self):
#         return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"
#
# # Testing the Rectangle class
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
#
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
# assert r4.get_square() == 32, 'Test4'
#
# assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
#
# print("All tests passed!")

#Hometask 15.2
from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        self.a = a
        self.b = b
        self.simplify()

    def simplify(self):
        common_divisor = gcd(self.a, self.b)
        self.a //= common_divisor
        self.b //= common_divisor

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.a, self.b * other.b)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.a * other.b + other.a * self.b
            new_denominator = self.b * other.b
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.a * other.b - other.a * self.b
            new_denominator = self.b * other.b
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a == other.a and self.b == other.b
        return False

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > other.a * self.b
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < other.a * self.b
        return NotImplemented

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

# Testing the Fraction class
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6', f'Test failed: {str(f_c)}'

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 1, 3', f'Test failed: {str(f_d)}'

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6', f'Test failed: {str(f_e)}'

assert f_d < f_c, f'Test failed: {f_d} < {f_c} expected True'
assert f_d > f_e, f'Test failed: {f_d} > {f_e} expected True'
assert f_a != f_b, f'Test failed: {f_a} != {f_b} expected True'

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2, f'Test failed: {f_1} == {f_2} expected True'

print('OK')
