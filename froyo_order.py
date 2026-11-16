class FroyoOrder:
    def __init__(self, flavor, topping, sauce, ounces):
        self.__flavor = flavor
        self.__topping = topping
        self.__sauce = sauce
        self.__ounces

    def self_flavor(self, flavor):
        self.__flavor = flavor

    def set_topping(self, topping):
        self.__topping = topping

    def set_sauce(self, sauce):
        self.__sauce = sauce

    def set_ounces(self, ounces):
        self.__ounces = ounces

    def get_flavor(self):
        return self.__flavor

    def get_topping(self):
        return self.__topping

    def get_sauce(self):
        return self.__sauce

    def get_ounces(self):
        return self.__ounces

    def display_order(self):
        print(f"1. Flavor(s): {self.__flavor}")
        print(f"2. Toppings: {self.__topping}")
        print(f"3. Sauce: {self.__sauce}")
        print(f"4. Ounces: {self.__ounces}")
