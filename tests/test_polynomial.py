import pytest

from minicas.polynomial import Polynomial
# ОБЯЗАТЕЛЬНО ИМПОРТИРУЕМ RATIONAL
from minicas.rational import Rational 

def test_degree():
    # Передаем список объектов Rational
    assert Polynomial([Rational(1), Rational(2), Rational(0), Rational(0)]).degree() == 1
    
def test_call():
    p = Polynomial([Rational(1), Rational(-3), Rational(2)])
    # Вызов p(2) вернет Rational(3), а p(0) -> Rational(1)
    assert p(2) == Rational(3)
    assert p(0) == Rational(1)
    
def test_add():
    p = Polynomial([Rational(1), Rational(-3), Rational(2)])
    q = Polynomial([Rational(0), Rational(1)])
    # Сравниваем коэффициенты со списком из Rational
    assert (p + q).coeffs == [Rational(1), Rational(-2), Rational(2)]
    
def test_mul():
    p = Polynomial([Rational(-1), Rational(1)])
    q = Polynomial([Rational(1), Rational(1)])
    assert (p * q).coeffs == [Rational(-1), Rational(0), Rational(1)]
    
def test_derivative():
    p = Polynomial([Rational(1), Rational(-3), Rational(2)])
    assert p.derivative().coeffs == [Rational(-3), Rational(4)]
    
def test_derivative_constant():
    # Производная константы вернет список с Rational(0)
    assert Polynomial([Rational(5)]).derivative().coeffs == [Rational(0)]

def test_str():
    # Этот тест останется без изменений, так как str() возвращает обычные строки!
    assert str(Polynomial([Rational(1), Rational(-3), Rational(2)])) == "2x^2 - 3x + 1"
    assert str(Polynomial([Rational(-1), Rational(1)])) == "x - 1"
    assert str(Polynomial([Rational(0)])) == "0"

def test_input_list_not_changed():
    # Исходный список тоже должен состоять из Rational
    coeffs = [Rational(1), Rational(2), Rational(0), Rational(0)]
    Polynomial(coeffs)
    assert coeffs == [Rational(1), Rational(2), Rational(0), Rational(0)]


# import pytest

# from minicas.polynomial import Polynomial

# def test_degree():
#     assert Polynomial([1, 2, 0, 0]).degree() == 1
    
# def test_call():
#     p = Polynomial([1, -3, 2])
#     assert p(2) == 3
#     assert p(0) == 1
    
# def test_add():
#     p = Polynomial([1, -3, 2])
#     q = Polynomial([0, 1])
#     assert (p + q).coeffs == [1, -2, 2]
    
# def test_mul():
#     p = Polynomial([-1, 1])
#     q = Polynomial([1, 1])
#     assert (p * q).coeffs == [-1, 0, 1]
    
# def test_derivative():
#     p = Polynomial([1, -3, 2])
#     assert p.derivative().coeffs == [-3, 4]
    
# def test_derivative_constant():
#     assert Polynomial([5]).derivative().coeffs == [0]


# def test_str():
#     assert str(Polynomial([1, -3, 2])) == "2x^2 - 3x + 1"
#     assert str(Polynomial([-1, 1])) == "x - 1"
#     assert str(Polynomial([0])) == "0"


# def test_input_list_not_changed():
#     coeffs = [1, 2, 0, 0]
#     Polynomial(coeffs)
#     assert coeffs == [1, 2, 0, 0]