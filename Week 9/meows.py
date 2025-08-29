import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()


for _ in range(int(args.n)):
    print("meow")














# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage: meows.py")





# def meow(n: int) -> str:
#     """
#     Meow n times.

#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError:
#     :return: A string of n meows, one per line
#     :rtype: str
#     """
#     return "meow\n" * n


# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")




# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")


# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)



# def meow(n: int):
#     for _ in range(n):
#         print("meow")


# number: int = int(input("Number: "))
# meow(number)



# class Cat:
#     MEOWS = 3


#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")


# cat = Cat()
# cat.meow()








# MEOWS = 3

# for _ in range(MEOWS):
#     print("meow")
