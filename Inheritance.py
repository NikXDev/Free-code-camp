class Chef:
    def make_chicken(self):
        print("The Chef Makes Chicken")

    def make_salad(self):
        print("The Chef Makes Salad")

    def make_special_dish(self):
        print("The Chef Makes Special Dish")


mychef = Chef()
mychef.make_special_dish()


class ChineseChef(Chef):
    def make_coronavirus(self):
        print("Opps...!!!!!")


mychinesechef = ChineseChef()
mychinesechef.make_chicken()