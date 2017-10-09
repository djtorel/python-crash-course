import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Does a city and country like 'Santiago, Chile' work?"""
        formatted_city_country = city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')


unittest.main()
