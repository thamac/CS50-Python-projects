def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Not an integer")


def main():
    height = 0

    while not (height >= 1 and height <= 8):
        height = get_int("Height: ")

    for i in range(height):
        print(" " * (height - i - 1), end="")
        print("#" * (i + 1), end="")
        print("  ", end="")
        print("#" * (i + 1))


main()
