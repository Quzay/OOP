import pytest

from app import Figure


@pytest.fixture
def square():
    return Figure("квадрат", 5)


def test_triangle_type():
    assert Figure("трикутник", 4).type == "трикутник"


@pytest.mark.parametrize("figure_type", Figure.FIGURES)
def test_allowed_figure(figure_type):
    assert Figure(figure_type, 1).type == figure_type


def test_square_length(square):
    assert square.get_figure_length == 5


def test_invalid_figure():
    with pytest.raises(AssertionError):
        Figure("коло", 1)

@pytest.fixture
def figure_length_10():
    return Figure("квадрат", 10)


def test_figure_length_10(figure_length_10):
    assert figure_length_10.get_figure_length == 10

def test_figure_type_length_10(figure_length_10):
    assert figure_length_10.type == "квадрат"

@pytest.mark.unit
def test_triangle_type():
    assert Figure("трикутник", 4).type == "трикутник"


@pytest.mark.unit
def test_invalid_figure():
    with pytest.raises(AssertionError):
        Figure("коло", 1)

@pytest.fixture(scope="module")
def allowed_figures():
    return Figure.FIGURES


def test_figures_count(allowed_figures):
    assert len(allowed_figures) == 3


def test_figures_contains_square(allowed_figures):
    assert "квадрат" in allowed_figures