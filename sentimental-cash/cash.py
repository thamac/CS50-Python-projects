def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not a float")


def main():
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1
    change = 0.0
    coins = 0

    while change <= 0.0:
        change = get_float("Change: ")

    change *= 100
    change = int(change)

    while change > 0.0:
        if change >= quarter:
            change -= quarter
            coins += 1
        elif change >= dime:
            change -= dime
            coins += 1
        elif change >= nickel:
            change -= nickel
            coins += 1
        elif change >= penny:
            change -= penny
            coins += 1

    print(coins)


main()
