import pytest
from app import Figure


# --- Ініціалізація ---

def test_square_created():
    f = Figure("квадрат", 5)
    assert f.type == "квадрат"
    assert f.length == 5

def test_invalid_length():
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)

def test_invalid_figure_type():
    with pytest.raises(AssertionError):
        Figure("коло", 5)


# --- get_angles ---

def test_square_angles():
    f = Figure("квадрат", 5)
    assert f.get_angles == 4

def test_rectangle_angles():
    f = Figure("прямокутник", 5)
    assert f.get_angles == 4

def test_triangle_angles():
    f = Figure("трикутник", 5)
    assert f.get_angles == 3