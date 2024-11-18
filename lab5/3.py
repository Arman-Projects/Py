from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator, self.denominator = self.reduction(numerator, denominator)

    def reduction(self, numerator, denominator):
        common_divisor = gcd(numerator, denominator)
        reduced_numerator = numerator // common_divisor
        reduced_denominator = denominator // common_divisor
        if reduced_denominator < 0:
            reduced_numerator = -reduced_numerator
            reduced_denominator = -reduced_denominator
        return reduced_numerator, reduced_denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ValueError("Cannot divide by zero fraction.")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < self.denominator * other.numerator
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator <= self.denominator * other.numerator
        return NotImplemented

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def to_float(self):
        return self.numerator / self.denominator

    def simplify(self):
        return Fraction(self.numerator, self.denominator)


frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

print(f"frac1: {frac1}")
print(f"frac2: {frac2}")

print(f"Addition: {frac1 + frac2}")
print(f"Subtraction: {frac1 - frac2}")
print(f"Multiplication: {frac1 * frac2}")
print(f"Division: {frac1 / frac2}")

frac3 = Fraction(6, 8)
print(f"Simplified frac3: {frac3}")

print(f"frac1 == frac2: {frac1 == frac2}")
print(f"frac1 < frac2: {frac1 < frac2}")
