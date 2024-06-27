class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(Animal: Animal):
    Animal.speak()


# dog = Dog()
# cat = Cat()
# make_noise(dog)
# make_noise(cat)
class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的核心制冷技术")

    def hot_wind(self):
        print("美的制热技术")

    def swing_l_r(self):
        print("美的左右摆风")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力制冷技术")

    def hot_wind(self):
        print("格力制热技术")

    def swing_l_r(self):
        print("格力左右摆风")


def make_cool(ac: AC):
    ac.cool_wind()


Midea = Midea_AC()
gree = GREE_AC()
make_cool(gree)
make_cool(Midea)
