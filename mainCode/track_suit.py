from mainCode import sportwear
from enum import Enum


class TrackSuit(sportwear.SportWear):
    def __init__(
        self, suit_size: str,
        persantage_of_cotton: int,
        price: float, brand, color, sex
    ):
        super().__init__(price, color, brand, sex)
        self.suit_size = suit_size
        self.persantage_of_cotton = persantage_of_cotton

    def get_suit_size(self):
        return self.suit_size

    def get_persantage_of_cotton(self):
        return self.persantage_of_cotton
