from enums import Enums
import mainCode
from mainCode import sportwear


class SportWearManager(mainCode.sportwear.SportWear):

    wears = []

    def set_wears(self, wears):
        self.wears = wears

    def get_wears(self):
        return self.wears

    # this function sort wears by  DESC and ASC price, if the set parameter order True it will  sort  by DESC
    # that`s why the func is  named in  such way. But you can sort wears ASC if you set order like False

    def sort_by_price_DESC(self, order):
        self.wears.sort(key=lambda c: c.get_price(), reverse=order)
        return self.wears

    # this function sort wears by  DESC and ASC price, if the set parameter order True it will  sort  by DESC
    # that`s why the func is  named in  such way. But you can sort wears ASC if you set order like False


    def sort_by_brand_DESC(self, order):
        self.wears.sort(key=lambda c: c.get_brand(), reverse=order)
        return self.wears

    def add_item(self, item):
        self.wears.append(item)
