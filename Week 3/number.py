def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()


# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#             return x
#         except ValueError:
#             print("x is not an integer")


# main()

# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")
