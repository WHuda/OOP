import pytest

from minicas.rational import Rational, RationalError


def test_creation_and_normalization():
    r = Rational(6, 3)
    assert r.num == 2
    assert r.den == 1

    r_neg = Rational(1, -2)
    assert r_neg.num == -1
    assert r_neg.den == 2

    assert Rational(5).den == 1


def test_zero_denominator():
    with pytest.raises(RationalError, match="нулевой знаменатель"):
        Rational(5, 0)


def test_negation():
    assert -Rational(1, 2) == Rational(-1, 2)
    assert -Rational(-3, 4) == Rational(3, 4)


def test_add():
    assert Rational(1, 3) + Rational(1, 3) == Rational(2, 3)
    assert Rational(1, 2) + Rational(1, 3) == Rational(5, 6)
    assert Rational(1, 2) + 2 == Rational(5, 2)
    assert 2 + Rational(1, 2) == Rational(5, 2)


def test_sub():
    assert Rational(1, 2) - Rational(1, 3) == Rational(1, 6)
    assert Rational(1, 2) - 1 == Rational(-1, 2)
    assert 1 - Rational(1, 2) == Rational(1, 2)


def test_mul():
    assert Rational(2, 3) * Rational(3, 4) == Rational(1, 2)
    assert Rational(2, 3) * 3 == Rational(2, 1)
    assert 3 * Rational(2, 3) == Rational(2, 1)


def test_div():
    assert Rational(1, 2) / Rational(1, 3) == Rational(3, 2)
    assert Rational(1, 2) / 2 == Rational(1, 4)
    assert 2 / Rational(1, 2) == Rational(4, 1)


def test_division_by_zero():
    with pytest.raises(RationalError, match="Деление на ноль"):
        Rational(1, 2) / Rational(0)

    with pytest.raises(RationalError, match="Деление на ноль"):
        2 / Rational(0)


def test_comparisons():
    assert Rational(1, 2) < Rational(2, 3)
    assert Rational(2, 3) > Rational(1, 2)
    assert Rational(1, 2) <= Rational(1, 2)
    assert Rational(1, 2) >= Rational(1, 2)
    assert Rational(1, 2) < 1
    assert 1 > Rational(1, 2)


def test_not_implemented():
    with pytest.raises(TypeError):
        _ = Rational(1, 2) + 0.5
    
    with pytest.raises(TypeError):
        _ = Rational(1, 2) < "string"


def test_float_and_abs():
    assert float(Rational(1, 2)) == 0.5
    assert abs(Rational(-5, 2)) == Rational(5, 2)


def test_str_and_repr():
    assert str(Rational(6, 3)) == "2"
    assert str(Rational(1, 2)) == "1/2"
    assert repr(Rational(1, 2)) == "Rational(num=1, den=2)"


def test_set_compatibility():
    s = {Rational(1, 2), Rational(1, 2), Rational(1, 3)}
    assert len(s) == 2


def test_equality_order_and_hash_with_int():
    one = Rational(2, 2)
    assert one == 1
    assert 1 == one
    assert one <= 1
    assert one >= 1
    assert not one < 1
    assert not one > 1
    assert hash(one) == hash(1)
    assert len({one, 1}) == 1


def test_str_of_large_integer_is_exact():
    value = 10**20 + 1
    assert str(Rational(value)) == str(value)
