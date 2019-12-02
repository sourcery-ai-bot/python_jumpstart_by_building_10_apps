import pathlib
import csv
import statistics
import data_types


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

        reader = csv.DictReader(fin)

        purchases = []

        for row in reader:
            p = data_types.Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases

        # print(purchases[0].__dict__)

        # for row in reader:
        #     print(f"Bed count: {row['beds']}, Type: {type(row['beds'])}")

        # general csv.reader()
        # header = fin.readline().strip()
        # reader = csv.reader(fin, delimiter=",")
        # for row in reader:
        #     print(type(row), row)


# def load_file_basic(filename):
#     with open(filename, "r", encoding="utf-8") as fin:
#         header = fin.readline().strip()
#         print(f"found header: {header}")

#         lines = []

#         for line in fin:
#             line_data = line.strip().split(",")
#             lines.append(line_data)

#         print(lines[:6])

#
# def get_price(p):
# return p.price
#


def query_data(data):
    # most expensive house ?

    data.sort(key=lambda p: p.price)
    high_purchase = data[-1]

    print(
        f"The most expensive house is ${high_purchase.price} with {high_purchase.beds} and {high_purchase.baths}."
    )
    # least expensive house ?

    low_purchase = data[0]
    print(
        f"The most least house is ${low_purchase.price} with {low_purchase.beds} and {low_purchase.baths}."
    )

    # average price house ?

    prices = [p.price for p in data]  # project of items  # set to process

    ave_price = statistics.mean(prices)
    print(f"The average home price is ${int(ave_price):,}.")

    prices = [p.price for p in data if p.beds == 2]

    # average price of 2 bedroom houses ?

    two_bed_homes = [p for p in data if p.beds == 2]
    # projection
    # source
    # filter

    avg_price = statistics.mean([p.price for p in two_bed_homes])
    avg_baths = statistics.mean([p.baths for p in two_bed_homes])
    avg_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])

    ave_price = statistics.mean(prices)
    print(
        f"The average price of a 2-bedroom home is ${int(ave_price):,} with baths={round(avg_baths, 1):,}, sq ft={round(avg_sqft, 1):,}."
    )


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


if __name__ == "__main__":
    main()
