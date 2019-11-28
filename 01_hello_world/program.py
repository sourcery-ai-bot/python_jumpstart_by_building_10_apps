def print_header():
    print("--------------------------------")
    print("            HELLO APP")
    print("--------------------------------")
    print()


def print_greeting():
    user_text = input("What is your name? ")
    greeting = f"Nice to meet you {user_text}."
    print(greeting)


def main():
    print_header()
    print_greeting()


if __name__ == "__main__":
    main()
