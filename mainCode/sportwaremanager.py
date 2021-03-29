from enums import Enums
import mainCode
from mainCode import sportwear


class SportWearManager(mainCode.sportwear.SportWear):

    wears = []

    def set_wears(self, wears):
        self.wears = wears

    def get_wears(self):
        return self.wears

    def sort_by_price(self, order):
        if order == Enums.SortType.ASC:
            self.wears(sorted(mainCode.sportwear.SportWear.get_price(self)))
        else:
            self.wears(sorted(mainCode.sportwear.SportWear.get_price(self), reverse=True))

    def sort_by_brand(self, order1):

        if order1 == Enums.Brand:
            self.wears(sorted(mainCode.sportwear.SportWear.get_brand(self)))
        else:
            self.wears(sorted(mainCode.sportwear.SportWear.get_brand(self), reverse=True))

    def add_item(self, item):
        self.wears.append(item)

