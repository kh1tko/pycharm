import unittest
from second import analyze_luggage


class TestLuggaageAnalasis(unittest.TestCase):
    def test_analyze_luggage(self):
        passengers_data = [
            {'number_of_items': 3, 'total_weight': 30},
            {'number_of_items': 2, 'total_weight': 20},
            {'number_of_items': 1, 'total_weight': 15},
            {'number_of_items': 6, 'total_weight': 95},
            {'number_of_items': 2, 'total_weight': 75},
            {'number_of_items': 5, 'total_weight': 35},
            # Додайте дані для ще пасажирів
        ]

        result = analyze_luggage(passengers_data)

        # Перевірка для категорії a)
        self.assertEqual(result[0], 3)

        # Перевірка для категорії b)
        self.assertTrue(result[1])

        # Перевірка для категорії c)
        self.assertEqual(result[2], 3)

    if __name__ == '__main__':
        unittest.main()
