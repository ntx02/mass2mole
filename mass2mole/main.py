#!/usr/bin/env python3

from convertclass import ConvertClass


def caller():
    print("Symbol of element?")
    elementsymbol = input().title()
    print("Weight of sample of element?")
    elementmass = input()
    testclass = ConvertClass(elementsymbol, elementmass)
    print(testclass.convert())


def main():
    while 1 == 1:
        print("Convert mass of element to moles? y/n")
        answer = input()
        if answer == "y":
            caller()
        else:
            break


if __name__ == "__main__":
    main()
