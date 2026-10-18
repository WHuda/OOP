import pytest

from minicas.polynomial import Polynomial
from minicas.rational import Rational


def test_degree():
    assert Polynomial([Rational(1), Rational(2), Rational(0), Rational(0)]).degree() == 1
    
def test_call():
    p = Polynomial([Rational(1), Rational(-3), Rational(2)])
    assert p(2) == Rational(3)
    assert p(0) == Rational(1)
    
def test_add():
    p = Polynomial([Rational(1), Rational(-3), Rational(2)])
    q = Polynomial([Rational(0), Rational(1)])
    assert (p + q).coeffs == [Rational(1), Rational(-2), Rational(2)]
    
def test_mul():
    p = Polynomial([Rational(-1), Rational(1)])
    q = Polynomial([Rational(1), Rational(1)])
    assert (p * q).coeffs == [Rational(-1), Rational(0), Rational(1)]
    
def test_derivative():
    p = Polynomial([Rational(1), Rational(-3), Rational(2)])
    assert p.derivative().coeffs == [Rational(-3), Rational(4)]
    
def test_derivative_constant():
    assert Polynomial([Rational(5)]).derivative().coeffs == [Rational(0)]

def test_str():
    assert str(Polynomial([Rational(1), Rational(-3), Rational(2)])) == "2x^2 - 3x + 1"
    assert str(Polynomial([Rational(-1), Rational(1)])) == "x - 1"
    assert str(Polynomial([Rational(0)])) == "0"

def test_input_list_not_changed():
    coeffs = [Rational(1), Rational(2), Rational(0), Rational(0)]
    Polynomial(coeffs)
    assert coeffs == [Rational(1), Rational(2), Rational(0), Rational(0)]


def test_integer_coefficients_still_work():
    coeffs = [0, 1, 0, 0]
    p = Polynomial(coeffs)
    assert p.coeffs == [Rational(0), Rational(1)]
    assert p.degree() == 1
    assert str(p) == "x"
    assert coeffs == [0, 1, 0, 0]
    assert Polynomial([0, 0]).degree() == 0
    assert str(Polynomial([0, 0])) == "0"

    product = Polynomial([-1, 1]) * Polynomial([1, 1])
    assert product.coeffs == [Rational(-1), Rational(0), Rational(1)]
    assert str(product) == "x^2 - 1"


def test_fractional_coefficients():
    p = Polynomial([Rational(1, 2), Rational(1, 3)])
    assert p(3) == Rational(3, 2)
    assert p.derivative().coeffs == [Rational(1, 3)]
    assert str(p) == "(1/3)x + 1/2"


def test_invalid_coefficient_is_rejected_early():
    with pytest.raises(TypeError, match="коэффициент"):
        Polynomial([0.5])
