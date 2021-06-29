from mainCode import sportwear, track_suit, sportshoes

def main():

    #making example object
    first_sportsuit = track_suit.TrackSuit(
        "L", 100, 1200, sportwear.Brand.Nike, "blue", sportwear.Sex.FEMALE
    )
    second_sportsuit = track_suit.TrackSuit(
        "M", 90, 2000, sportwear.Brand.Adidas, "red", sportwear.Sex.MALE
    )
    first_sportshoes = sportshoes.SportShoes(
        36, 1455, sportwear.Brand.Asics, "red", sportwear.Sex.UNISEX
    )
    second_sportshoes = sportshoes.SportShoes(
        36, 1455, sportwear.Brand.Asics, "red", sportwear.Sex.UNISEX
    )


