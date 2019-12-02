import pathlib


def print_header():
    print("--------------------------------")
    print(" REAL ESTATE DATA MINING APP")
    print("--------------------------------")
    print()


def get_data_file():
    path = pathlib.Path("./data/SacramentoRealEstateTransactions2008.csv")
    return path.absolute()


def load_file(filename):
    with open(filename, "r", encoding="utf-8") as fin:
        for line in fin:
            print(line)
            break


def query_data(data):
    pass


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


if __name__ == "__main__":
    main()
