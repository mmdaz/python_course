def lcm(x, y):
    from math import gcd
    return x * y // gcd(x, y)


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __add__(self, other):
        common = lcm(self.denominator, other.denominator)
        return Fraction(
            numerator=((common / self.denominator) * self.numerator + (common / other.denominator) * other.numerator),
            denominator=common)

    def __sub__(self, other):
        common = lcm(self.denominator, self.numerator)
        return Fraction(
            numerator=((common / self.denominator) * self.numerator - (common / other.denominator) * other.numerator),
            denominator=common)

    def __eq__(self, other):
        common = lcm(self.denominator, other.denominator)
        return (common / self.denominator) * self.numerator == (common / other.denominator) * other.numerator

    def product(self, other):
        return Fraction(numerator=self.numerator * other.numerator, denominator=self.denominator * other.denominator)


f1 = Fraction(1, 4)
f2 = Fraction(2, 4)

print(f1.product(f2))
