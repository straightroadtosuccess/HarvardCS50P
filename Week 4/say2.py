import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.tux("hello, " + sys.argv[1])


# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])
