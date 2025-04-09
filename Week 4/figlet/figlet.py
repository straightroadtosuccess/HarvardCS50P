from pyfiglet import Figlet
import sys

figlet = Figlet()


def main():
    # add argvs to define font style, usage and sys.exit
    if "-f" in sys.argv:
        x = sys.argv[2]
        f = Figlet(font=x)
    else:
        sys.exit("Invalid usage ")

    # Get input from the awesome user!
    text = input("Input: ")

    # Print list of available fonts
    # print(figlet.getFonts())
    print(f.renderText(text))


main()
