from enums import Enums
from mainCode import sportwear


class SportWearManager(sportwear.SportWear):

    def __init__(self, wears):
        self.wears = wears
    wears = []

    # this function sort wears by  DESC and ASC price,
    # if the set parameter order True it will  sort  by DESC
    # that`s why the func is  named in  such way.
    # But you can sort wears ASC if you set order like False

    def sort_by_price(self, order):
        if order == Enums.SortType.ASC:
            self.wears.sort(key=lambda c: c.get_price())
        else:
            self.wears.sort(key=lambda c: c.get_price(), reverse=True)

    # this function sort wears by  DESC and ASC price,
    # if the set parameter order True it will  sort  by DESC
    # that`s why the func is  named in  such way.
    # But you can sort wears ASC if you set order like False

    def search_by_brand(self, brand):
        searched_brand = []
        for items in self.wears:
            if items.get_brand() == brand:
                searched_brand.append(items)
        return searched_brand

    def add_item(self, item):
        self.wears.append(item)
