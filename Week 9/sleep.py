def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "bah" * 1


if __name__ == "__main__":
    main()




def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("bah" * i)
#     return flock


# if __name__ == "__main__":
#     main()
