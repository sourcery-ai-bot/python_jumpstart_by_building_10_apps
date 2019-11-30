def print_header():
    print("--------------------------------")
    print("           JOURNAL APP")
    print("--------------------------------")
    print()


def run_event_loop():
    print("What do you want to do with your journal? ")

    cmd = None

    journal_data = []

    while cmd != "x":
        cmd = input("[L]ist entries, [A]dd an entry, E[x]it: ")
        cmd = cmd.lower().strip()

        if cmd == "l":
            list_entries(journal_data)
        elif cmd == "a":
            add_entries(journal_data)
        elif cmd != "x":
            print(f"Sorry, we dont understand '{cmd}'.")

    print("Done. Goodbye.")


def list_entries(data):
    print("Your journal entries: ")
    entries = reversed(data)
    for idx, entry in enumerate(entries, 1):
        print(f"* [{idx}]: {entry}")


def add_entries(data):
    text = input("Type your entry, <enter> to exit: ")
    data.append(text)


def main():
    print_header()
    run_event_loop()


if __name__ == "__main__":
    main()
