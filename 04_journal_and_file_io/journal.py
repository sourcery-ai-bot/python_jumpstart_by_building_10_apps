import os


def load(name):
    # todo: populate from file if it exists.
    return []


def save(name, journal_data):
    filename = os.path.abspath(os.path.join(".", "journals", name + ".jrl"))
    print(f".... saving to: {filename}")

    with open(filename, "w") as fout:
        for entry in journal_data:
            fout.write(entry + "\n")


def add_entry(text, journal_data):
    return journal_data.append(text)

