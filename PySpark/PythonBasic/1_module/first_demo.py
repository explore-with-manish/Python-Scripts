"""This module demonstrates use of print method"""


def string_reverse(str1):
    """
    Returns the reversed String.

    Parameters:
        str1 (str):The string which is to be reversed.

    Returns:
        reverse(str1):The string which gets reversed.
    """
    reverse_str1 = ""
    i = len(str1)
    while i > 0:
        reverse_str1 += str1[i - 1]
        i = i - 1
    return reverse_str1


def main():
    """Main function to demonstrate the usage"""
    r_str = string_reverse("Hello World!")
    print(r_str)


if __name__ == "__main__":
    main()

# print(__name__)
