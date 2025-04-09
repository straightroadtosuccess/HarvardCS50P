def main():
	number = get_number()
	meow(number)

def get_number():
	while True:
		n = int(input("What's n? "))
		if n > 0:
			break
	return n

def meow(n):
	for _ in range(n):
		print("meow")

main()

# def main():
# 	number = get_number
# 	meow(3)

# def meow(n):
# 	for _ in range(n):
# 		print("meow")

# main()

# while True:
# 	n = int(input("What's n? "))
# 	if n > 0:
# 		break

# for _ in range(n):
# 	print("meow")



# n = input("What's n? ")

# if n < 0:
# 	n = input(input("What's n"))
# 	if n < 0:
# 		n = int()


# print("meow\n" * 3, end="")

# for i in [0, 1, 2]:
# 	print("meow")

# for i in range(3):
#     print("meow")


# i = 0
# while i < 3:
#     print("meow")
#     i = i + 1

# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1



# print("meow")
# print("meow")
# print("meow")
