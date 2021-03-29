from mainCode import sportwear


class SportShoes(sportwear.SportWear):
    def __init__(self, shoes_size: float, price, brand, color, sex):
        super().__init__(brand,price,color,sex)
        self.shoes_size = shoes_size


    def get_shoes_size(self):
        return self.shoes_size  










