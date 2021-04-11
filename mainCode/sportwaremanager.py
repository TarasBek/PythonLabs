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
            self.wears.sort(key=lambda c: c.get_price())
        else:
            self.wears.sort(key=lambda c: c.get_price(), reverse=True)

    def sort_by_brand(self, order):

       if order == Enums.SortType.ASC:
        self.wears.sort(key=lambda c: c.get_brand())

       else:
        self.wears.sort(key=lambda c: c.get_brand(), reverse=True)

    def add_item(self, item):
        self.wears.append(item)
