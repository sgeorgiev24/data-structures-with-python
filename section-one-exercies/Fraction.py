import math


class Fraction:
    def __init__(self, exponent, fraction):
        if not isinstance(exponent, int) or not isinstance(fraction, int):
            raise TypeError("Exponent and fraction should be int.")

        common = math.gcd(exponent, fraction)

        self.exponent = exponent // common
        self.fraction = fraction // common

    def __add__(self, otherFraction):
        newExponent = self.exponent * otherFraction.fraction + \
            otherFraction.exponent * self.fraction
        newFraction = self.fraction * otherFraction.fraction

        return Fraction(newExponent, newFraction)

    def __radd__(self, num):
        return self + Fraction(num, 1)

    def __sub__(self, otherFraction):
        newExponent = self.exponent * otherFraction.fraction - \
            otherFraction.exponent * self.fraction
        newFraction = self.fraction * otherFraction.fraction

        return Fraction(newExponent, newFraction)

    def __mul__(self, otherFraction):
        newExponent = self.exponent * otherFraction.exponent
        newFraction = self.fraction * otherFraction.fraction

        return Fraction(newExponent, newFraction)

    def __truediv__(self, otherFraction):
        xFraction = Fraction(otherFraction.fraction, otherFraction.exponent)

        return self * xFraction

    def __eq__(self, otherFraction):
        return self.exponent * otherFraction.fraction == \
            self.fraction * otherFraction.exponent

    def __str__(self):
        return str(self.exponent) + "/" + str(self.fraction)

    def getNum(self):
        return self.exponent

    def getDen(self):
        return self.fraction
