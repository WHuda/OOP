from minicas.rational import Rational 
class Polynomial:

    def __init__(self, coeffs: list[Rational] | None = None):
        if coeffs is None:
            coeffs = []
        # Копируем список, чтобы не испортить исходный
        self.coeffs = self.remove_zeroes(coeffs.copy())

    def remove_zeroes(self, coeffs: list[Rational]) -> list[Rational]:
        # Удаляем лишние старшие нули, сравнивая с Rational(0)
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
        max_len = max(len(self.coeffs), len(other.coeffs))
        new_coeffs = []
        for i in range(max_len):
            # Дополняем недостающие коэффициенты объектами Rational(0)
            c1 = self.coeffs[i] if i < len(self.coeffs) else Rational(0)
            c2 = other.coeffs[i] if i < len(other.coeffs) else Rational(0)
            new_coeffs.append(c1 + c2)
            
        return Polynomial(new_coeffs)
            
    def __str__(self) -> str:
        terms = []

        for i in range(len(self.coeffs) - 1, -1, -1):
            coeff = self.coeffs[i]

            # Корректное сравнение с нулевой дробью
            if coeff == Rational(0):
                continue

            abs_coeff = abs(coeff)

            # Корректное сравнение с единичной дробью Rational(1)
            if i == 0:
                term = f"{abs_coeff}"
            elif i == 1:
                term = "x" if abs_coeff == Rational(1) else f"{abs_coeff}x"
            else:
                term = f"x^{i}" if abs_coeff == Rational(1) else f"{abs_coeff}x^{i}"

            if not terms:
                # Проверяем знак дроби (сравниваем с нулем)
                if coeff < Rational(0):
                    term = "-" + term
            else:
                term = ("- " if coeff < Rational(0) else "+ ") + term

            terms.append(term)

        return " ".join(terms) if terms else "0"

    def __mul__(self, other) -> "Polynomial":
        new_len = len(self.coeffs) + len(other.coeffs) - 1
        # Инициализируем результирующий список строго объектами Rational(0)
        new_coeffs = [Rational(0)] * new_len
        
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                new_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]

        return Polynomial(new_coeffs)

    def derivative(self) -> "Polynomial":
        new_coeffs = []
        
        for i in range(1, len(self.coeffs)):
            # Работает благодаря поддержке умножения int * Rational
            new_coeffs.append(i * self.coeffs[i])
            
        return Polynomial(new_coeffs)

    def __call__(self, other) -> Rational:
        # Инициализируем аккумулятор типом Rational(0)
        result = Rational(0)
        for coeff in reversed(self.coeffs):
            result = result * other + coeff
        return result
    
    def __repr__(self):
        return f"Polynomial({self.coeffs})"
