from enums.Enums import Brand, Sex


class SportWear:

    def __init__(self, price: float, color: str, brand: Brand, sex: Sex):
        self.price = price
        self.color = color
        self.brand = brand
        self.sex = sex

    def get_price(self):
        return self.price

    def get_color(self):
        return self.color

    def get_brand(self):
        return self.brand

    def get_sex(self):
        return self.sex


if __name__ == '__main__':
    pass
