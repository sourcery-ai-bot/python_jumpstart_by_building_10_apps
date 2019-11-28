import random


def print_header():
    print("--------------------------------")
    print("GUESS THAT NUMBER GAME")
    print("--------------------------------")
    print()


def generate_random_number():
    return random.randint(0, 100)


def guess_the_number(the_number):

    guess = None
    name = input("Enter your name? ")

    while guess != the_number:

        guess_text = input("Guess a number between 0 and 100: ")
        guess = int(guess_text)

        if guess < the_number:
            print(f"{name} your guess of {guess} is too LOW.")
        elif guess > the_number:
            print(f"{name} your guess of {guess} is too HIGH.")
        else:
            print(f"{name} your guess of {guess} is the WINNER!")


def main():
    print_header()
    the_number = generate_random_number()
    guess_the_number(the_number)


if __name__ == "__main__":
    main()
