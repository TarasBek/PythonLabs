from mainCode import sportwear, track_suit, sportshoes, sportwaremanager
from enums import Enums

def main():

    one_sportsuit = track_suit.TrackSuit("L", 100, 1200, sportwear.Brand.Nike, "blue", sportwear.Sex.FEMALE)
    one_sportshoes = sportshoes.SportShoes(36, 1455, sportwear.Brand.Asics, "red", sportwear.Sex.UNISEX)

    manager = sportwaremanager.SportWearManager(price=True,  brand = True, sex=True, color=True)
    manager.add_item(one_sportsuit)
    manager.sort_by_brand(one_sportshoes)
    manager.sort_by_price(one_sportsuit)


    for a  in  manager.sort_by_brand(Enums.Brand.Asics):

        print(a)




    return manager.sort_by_brand(one_sportshoes)
if __name__ == '__main__':
    main()
