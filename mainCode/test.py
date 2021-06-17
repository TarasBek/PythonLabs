import unittest
from mainCode import sportwear, track_suit, sportshoes, sportwaremanager
from enums import Enums


class TestUnderwearManager(unittest.TestCase):
    def setUp(self):
        self.first_sportsuit = track_suit.TrackSuit(
            "L", 100, 1200, sportwear.Brand.Nike, "blue", sportwear.Sex.FEMALE
        )
        self.second_sportsuit = track_suit.TrackSuit(
            "M", 90, 2000, sportwear.Brand.Adidas, "red", sportwear.Sex.MALE
        )
        self.first_sportshoes = sportshoes.SportShoes(
            36, 1455, sportwear.Brand.Asics, "red", sportwear.Sex.UNISEX
        )
        self.second_sportshoes = sportshoes.SportShoes(
            36, 1455, sportwear.Brand.Asics, "red", sportwear.Sex.UNISEX
        )
        self.brand = Enums.Brand.Puma
        wears = [self.first_sportsuit, self.second_sportsuit]
        self.sportwaremanager = sportwaremanager.SportWearManager(wears)

    def test_sort_by_price(self):
        self.assertEqual(
            self.sportwaremanager.sort_by_price(Enums.SortType.ASC), [self.first_sportsuit, self.second_sportsuit]
                )

    def test_search_by_brand(self):
        self.assertEqual(self.sportwaremanager.search_by_brand(self.brand), True)


if __name__ == "__main__":
    unittest.main()
