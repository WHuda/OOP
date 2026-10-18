from minicas.rational import Rational


class Polynomial:

    def __init__(self, coeffs: list[Rational | int] | None = None):
        if coeffs is None:
            coeffs = []

        rational_coeffs = []
        for coeff in coeffs:
            if isinstance(coeff, Rational):
                rational_coeffs.append(coeff)
            elif isinstance(coeff, int):
                rational_coeffs.append(Rational(coeff))
            else:
                raise TypeError("коэффициент должен быть int или Rational")

        self.coeffs = self.remove_zeroes(rational_coeffs)

    def remove_zeroes(self, coeffs: list[Rational]) -> list[Rational]:
        coeffs = coeffs.copy()
        while len(coeffs) > 1 and coeffs[-1] == Rational(0):
            coeffs.pop()

        if not coeffs:
            return [Rational(0)]
        return coeffs

    def degree(self) -> int:
        if len(self.coeffs) == 1 and self.coeffs[0] == Rational(0):
            return 0
        return len(self.coeffs) - 1

    def __add__(self, other) -> "Polynomial":
        if not isinstance(other, Polynomial):
            return NotImplemented

        max_len = max(len(self.coeffs), len(other.coeffs))
        new_coeffs = []
        for i in range(max_len):
            c1 = self.coeffs[i] if i < len(self.coeffs) else Rational(0)
            c2 = other.coeffs[i] if i < len(other.coeffs) else Rational(0)
            new_coeffs.append(c1 + c2)

        return Polynomial(new_coeffs)

    def __str__(self) -> str:
        terms = []

        for i in range(len(self.coeffs) - 1, -1, -1):
            coeff = self.coeffs[i]

            if coeff == Rational(0):
                continue

            abs_coeff = abs(coeff)

            if i == 0:
                term = str(abs_coeff)
            else:
                power = "x" if i == 1 else f"x^{i}"
                if abs_coeff == Rational(1):
                    term = power
                else:
                    coeff_text = str(abs_coeff)
                    if abs_coeff.den != 1:
                        coeff_text = f"({coeff_text})"
                    term = f"{coeff_text}{power}"

            if not terms:
                if coeff < Rational(0):
                    term = "-" + term
            else:
                term = ("- " if coeff < Rational(0) else "+ ") + term

            terms.append(term)

        return " ".join(terms) if terms else "0"

    def __mul__(self, other) -> "Polynomial":
        if not isinstance(other, Polynomial):
            return NotImplemented

        new_len = len(self.coeffs) + len(other.coeffs) - 1
        new_coeffs = [Rational(0)] * new_len

        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                new_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]

        return Polynomial(new_coeffs)

    def derivative(self) -> "Polynomial":
        new_coeffs = []

        for i in range(1, len(self.coeffs)):
            new_coeffs.append(i * self.coeffs[i])

        return Polynomial(new_coeffs)

    def __call__(self, other) -> Rational:
        result = Rational(0)
        for coeff in reversed(self.coeffs):
            result = result * other + coeff
        return result

    def __repr__(self):
        return f"Polynomial({self.coeffs})"
