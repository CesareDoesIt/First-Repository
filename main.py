"""

    Welcome to Cesare's Inventory Management System (CIMS).

    MENU
    1. Add an entry
    2. List all existing entries
    3. Search

    ...

    1. Vacuum cleaner
    2. Bike jack
    3. M6 screw
    4. Pizza
    5. Keychain
    ...
    12. Car tires

    Input your command (enter b to go back to main menu): d 1
    Are you sure you want to delete the "Vacuum cleaner" (Y/N)?: Y
    "Vacuum cleaner" deleted
"""


def wrong_character():
    print "Please enter number from menu"


def menu(items):
    while True:
        for (index, item) in enumerate(items):
            print(str(index + 1) + ". " + item.upper())

        selection_index = int(raw_input("> ")) - 1

        if selection_index < 0 or selection_index > len(items) - 1:
            wrong_character()
            continue

        return selection_index

# function that returns string in reverse
# functon that returns true if two lists are identical or false other wise
# implement enumerate function without using the built-in enumerate()
# implement a function that calculates number of WORDS in a string
# function that takes a string and returns a list of each word in the string

"how are you"
["how", "are", "you"]


def length(items):
    count = 0

    for item in items:
        count += 1

    return count


def recursive_len(items):
    if items == []:
        return 0
    else:
        return recursive_len(items[:-1]) + 1


def split(s):
    words = []
    buffer = ""

    for character in s:
        if character == " ":  # whatever came before this, was a word
            words.append(buffer)
            buffer = ""
        else:
            buffer = buffer + character

    if buffer != "":
        words.append(buffer)

    return words

def wordcount(s):
    words = split(s)

    return len(words)



def main():
    # Main entry point
    main_menu_items = [
        "Add an entry",
        "List all entries",
        "Search for specific entry",
        "Maybe something different"
    ]

    # selection_index = menu(main_menu_items)

    # print("You selected item '" + main_menu_items[selection_index] + "'")
    print(split(main_menu_items[2]))


if __name__ == "__main__":
    main()
