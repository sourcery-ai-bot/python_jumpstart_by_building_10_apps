import actors
import random
import time


def print_header():
    print("----------------------------------")
    print("        WIZARD GAME APP")
    print("----------------------------------")
    print()


def game_loop():

    creatures = [
        actors.SmallAnimal("Toad", 1),
        actors.Creature("Tiger", 12),
        actors.SmallAnimal("Bat", 3),
        actors.Dragon("Dragon", 50, 75, True),
        actors.Wizard("Evil Wizard", 1000),
    ]

    hero = actors.Wizard("Gandolf", 75)

    while True:

        active_creature = random.choice(creatures)
        print(
            f"A {active_creature.name} of level {active_creature.level} has appeared from a dark and foggy forest.."
        )
        print()

        cmd = input("Do you [a]tack, [r]unaway or [l]ook around? ").strip()

        if cmd == "a":

            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The Wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("THe Wizard returns revitalized!!")

        elif cmd == "r":
            print("The Wizard has become unsure of his power and flees.")

        elif cmd == "l":
            print(f"The Wizard {hero.name} take in the surroundings and sees:")

            for c in creatures:
                print(f"* A {c.name} of level {c.level}")
        else:
            print("Ok, exiting game... bye!")
            break

        if not creatures:
            print("You defeated all the creatures, well done.")
            break

        print()


def main():
    print_header()
    game_loop()


if __name__ == "__main__":
    main()
