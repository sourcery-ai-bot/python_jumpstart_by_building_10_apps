import os
import pathlib


# TODO: replace os.path with pathlib


def load(name):
    data = []
    filename = get_full_pathname(name)
    path = pathlib.Path(filename)

    if path.exists:
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print(f".... saving to: {filename}")

    with open(filename, "w") as fout:
        for entry in journal_data:
            fout.write(entry + "\n")


def get_full_pathname(name):
    return os.path.abspath(os.path.join(".", "journals", name + ".jrl"))


def add_entry(text, journal_data):
    return journal_data.append(text)

