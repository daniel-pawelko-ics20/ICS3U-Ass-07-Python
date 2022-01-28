#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Assignment 7


def biggest(inp):
    # find biggest
    largest = inp[0]

    # process
    for num in inp:
        if num > largest:
            largest = num

    # return largest
    return largest


def main():
    # main function, calling biggest

    # variable
    number_list = []

    try:
        # input
        while True:
            inp = input("Enter a number: ")
            number_list.append(float(inp))
    except Exception:
        # output/calling biggest
        print(f"Biggest number is {biggest(number_list)}")

    # done
    print("\nDone.")


if __name__ == "__main__":
    main()
