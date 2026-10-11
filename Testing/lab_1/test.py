import unittest
from unittest.mock import patch
from app import Figure


class TestFigure(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Figure("квадрат", 5)

    def test_figure_type(self):
        self.assertEqual("квадрат", self.obj.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(5, self.obj.get_figure_length)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

    def test_invalid_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)

    # ⭐ get_angles
    def test_angles_square(self):
        self.assertEqual(4, Figure("квадрат", 5).get_angles())

    def test_angles_rectangle(self):
        self.assertEqual(4, Figure("прямокутник", 5).get_angles())

    def test_angles_triangle(self):
        self.assertEqual(3, Figure("трикутник", 5).get_angles())

    # ⭐ subTest
    def test_all_figure_types(self):
        for figure in Figure.FIGURES:
            with self.subTest(figure=figure):
                self.assertEqual(figure, Figure(figure, 5).get_figure_type)

    # ⭐ patch
    @patch("builtins.input", return_value="5")
    def test_input(self, mock_input):
        self.assertEqual("5", input("Введіть число: "))
        mock_input.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)