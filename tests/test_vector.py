from minicas.vector import Vector2D


def test_length():
    assert Vector2D(3, 4).length() == 5
    
def test_scaled_returns_new_vector():
    v = Vector2D(1, 2)
    w = v.scaled(3)
    assert (w.x, w.y) == (3, 6)
    assert (v.x, v.y) == (1, 2) # исходный вектор не изменился
    
def test_reprt():
    assert repr(Vector2D(1, 2)) == "Vector2D(1, 2)"
    
    