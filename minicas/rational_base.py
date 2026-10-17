from dataclasses import dataclass
from functools import total_ordering
from math import gcd


class RationalError(ArithmeticError):
    """Ошибка при работе с рациональными числами."""


@total_ordering
@dataclass(frozen=True)
class Rational:
    num: int
    den: int = 1

    def __post_init__(self):
        if self.den == 0:
            raise RationalError("нулевой знаменатель")
        g = gcd(self.num, self.den)
        sign = -1 if self.den < 0 else 1
        object.__setattr__(self, "num", sign * self.num // g)
        object.__setattr__(self, "den", sign * self.den // g)

    def __neg__(self):
        return Rational(-self.num, self.den)

    def __sub__(self, other: list) -> "Rational":
        if isinstance(other, float | int):
            other = Rational(other, 1)
        if self.den == other.den:
            return Rational(self.num - other.num, self.den)
        new_num1 = self.num * other.den
        new_num2 = other.num * self.den
        return Rational(new_num1 - new_num2, self.den * other.den)

    def __rsub__(self, other):
        if isinstance(other, float | int):
            other = Rational(other, 1)
        new_num1 = other.num * self.den
        new_num2 = self.num * other.den
        return Rational(new_num1 - new_num2, self.den * other.den)

    def __lt__(self):
        pass

    def __truediv__(self, other):
        if isinstance(other, float | int):
            other = Rational(other, 1)
        return Rational(self.num * other.den, self.den * other.num)

    def __rtruediv__(self, other):
        if isinstance(other, float | int):
            other = Rational(other, 1)
        return Rational(self.den * other.num, self.num * other.den)

    def __add__(self, other):
        if isinstance(other, float | int):
            other = Rational(other, 1)
        if self.den == other.den:
            return Rational(self.num + other.num, self.den)
        new_num1 = self.num * other.den
        new_num2 = other.num * self.den
        return Rational(new_num1 + new_num2, self.den * other.den)

    __radd__ = __add__

    def __str__(self):
        if self.num % self.den == 0:
            return f"{int(self.num/self.den)}"
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Rational(num={self.num}, den={self.den})"


r1 = Rational(6, 3)
r2 = Rational(1, 2)
print(-r1)
