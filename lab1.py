class Dryer:
    price = 100

    def __init__(self, electricity_consumption, max_load, weight):
        self.electricity_consumption = electricity_consumption
        self.max_load = max_load
        self.weight = weight

    def __str__(self):
        return f"Electricity consumption: {self.electricity_consumption}\n" \
               f"Maximum load: {self.max_load}\n" \
               f"Weight: {self.weight}\n"

    def __del__(self):
        print("викликався десткуктор")
        return

    @staticmethod
    def dryer_price():
        return Dryer.price


def main():
    object1 = Dryer, ("43 W/h", "15 kg", "220 kg")
    print(object1.__str__())

    object2 = Dryer("30 W/h", "7 kg", "210 kg")
    print(object2.__str__())

    object3 = Dryer("35 W/h", "9 kg", "150 kg")
    print(object3.__str__(),f"3 object price{object3.price}\n")


if __name__ == '__main__':
    main()
