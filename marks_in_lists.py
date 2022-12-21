#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in December 2022
# A program that puts marks in a list and calculates the average of the list


def find_average_in_a_list(list):
    # Calculates the average of a list

    sum = 0
    average = 0

    for number in list:
        sum += number
    average = sum / len(list)
    # Formats integers correctly
    if average % 1 == 0:
        average = int(average)

    return average


def main():
    # Gets marks, puts the marks in a list and calls the average function

    mark_list = []
    print("Enter marks | Enter a negative number to stop\n")
    while True:
        try:
            mark_text = input("Enter a mark percent: ")
            mark_int = int(mark_text)
            if mark_int >= 0 and mark_int <= 100:
                mark_list.append(mark_int)
            elif mark_int > 100:
                print("\nThis isn't a valid mark.\n")
            else:
                break
        except ValueError:
            print("\nThis isn't a valid mark.\n")
    mark_average = find_average_in_a_list(mark_list)
    text = "\nThe mark average is "
    if mark_average % 1 == 0:
        text += str(mark_average)
    else:
        text += "{:.2f}".format(mark_average)
    print(text + ".")

    print("\nDone.")


if __name__ == "__main__":
    main()
