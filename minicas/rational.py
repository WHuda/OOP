from dataclasses import dataclass
from functools import total_ordering
from math import gcd


class RationalError(ArithmeticError):
    """Ошибка при работе с рациональными числами."""

@total_ordering
@dataclass(frozen=True)
class Rational:
    """Неизменяемая рациональная дробь в сокращённом виде."""

    num: int
    den: int = 1

    def __post_init__(self):
        if self.den == 0:
            raise RationalError("нулевой знаменатель")
        g = gcd(self.num, self.den)
        sign = -1 if self.den < 0 else 1
        object.__setattr__(self, "num", sign * self.num // g)
        object.__setattr__(self, "den", sign * self.den // g)


    def __neg__(self) -> "Rational":
        return Rational(-self.num, self.den)

    def __sub__(self, other) -> "Rational":
        if isinstance(other, int):
            other = Rational(other, 1)
        if not isinstance(other, Rational):
            return NotImplemented
        
        return self + (-other)


    def __rsub__(self, other) -> "Rational":
        if isinstance(other, int):
            other = Rational(other, 1)
        if not isinstance(other, Rational):
            return NotImplemented

        return other + (-self)

    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            return self.den == 1 and self.num == other
        if isinstance(other, Rational):
            return self.num == other.num and self.den == other.den
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.num) if self.den == 1 else hash((self.num, self.den))

    def __lt__(self, other) -> bool:
        if isinstance(other, int):
            other = Rational(other, 1)
        if not isinstance(other, Rational):
            return NotImplemented

        return self.num * other.den < other.num * self.den

    def __mul__(self, other) -> "Rational":
        if isinstance(other, int):
            other = Rational(other, 1)
        if not isinstance(other, Rational):
            return NotImplemented


        return Rational(self.num * other.num, self.den * other.den)

    __rmul__ = __mul__

    def __truediv__(self, other) -> "Rational":
        if isinstance(other, int):
            other = Rational(other, 1)
        if not isinstance(other, Rational):
            return NotImplemented
        
        if other.num == 0:
            raise RationalError("Деление на ноль")
            
        return Rational(self.num * other.den, self.den * other.num)

    def __rtruediv__(self, other) -> "Rational":
        if isinstance(other, int):
            other = Rational(other, 1)
        if not isinstance(other, Rational):
            return NotImplemented

        if self.num == 0:
            raise RationalError("Деление на ноль")

        return Rational(other.num * self.den, other.den * self.num)

    def __add__(self, other) -> "Rational":
        if isinstance(other, int):
            other = Rational(other, 1)
        if not isinstance(other, Rational):
            return NotImplemented

        if self.den == other.den:
            return Rational(self.num + other.num, self.den)

        new_num1 = self.num * other.den
        new_num2 = other.num * self.den
        return Rational(new_num1 + new_num2, self.den * other.den)

    __radd__ = __add__

    def __float__(self) -> float:
        return self.num / self.den

    def __abs__(self) -> "Rational":
        return Rational(abs(self.num), self.den)

    def __str__(self) -> str:
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        return f"Rational(num={self.num}, den={self.den})"
