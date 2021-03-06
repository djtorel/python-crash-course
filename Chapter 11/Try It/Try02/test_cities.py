import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Does a city and country like 'Santiago, Chile' work?"""
        formatted_city_country = city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """
        Does a city, country, and population like
        'Santiago, Chile - population 5000000' work?
        """
        formatted_city_country = city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city_country,
                         'Santiago, Chile - population 5000000')


unittest.main()
