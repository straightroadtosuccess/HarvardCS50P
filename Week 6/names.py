names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")










# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names, reverse=True):
#     print(f"hello, {name}")

# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip())





# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())




# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip())



# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")



# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()


# names = []

# for _ in range(3):
#     names.append(input("What's your name: "))

# for name in sorted(names):
#     print(f"hello, {name}")

# for _ in range(3):
#     name = input("What's your name: ")
#     names.append(name)


# print(f"hello, {name}")
