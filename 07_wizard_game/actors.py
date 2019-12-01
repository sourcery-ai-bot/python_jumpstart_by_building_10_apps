import random


class Creature(object):
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"Creature: {self.name} of level {self.level}"

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def attack(self, creature):
        print(f"The wizard {self.name} attacks {creature}")

        my_roll = random.randint(1, 12) * self.level
        creature_roll = self.get_defensive_roll()

        print(f"You roll {my_roll}")
        print(f"{creature.name} rolls {creature_roll}")

        if my_roll > creature_roll:
            print(f"The Wizard has handily triumphed over {creature.name}")
            return True
        else:
            print("The Wizard has been defeated!!")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()

        # fire_modifier = 1
        # if self.breaths_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1

        # fire_modifier = VALUE_IF_TRUE if SOME_TEST else VALUE_IF_TRUE
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier

