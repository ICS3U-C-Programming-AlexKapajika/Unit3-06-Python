#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Oct 24, 2023
# This program use the try statement


def main():
    # this function uses a try statement

    integer_as_string = input("Enter an integer: ")
    print("")

    # process and output
    try:
        integer_as_string = int(integer_as_string)
        print("You entered an integer correctly")
    except Exception:
        print("This this was not")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
