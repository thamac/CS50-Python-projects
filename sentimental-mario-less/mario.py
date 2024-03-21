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

    for j in range(height):
        print(" " * (height - j - 1), end="")
        print("#" * (j + 1))


main()
