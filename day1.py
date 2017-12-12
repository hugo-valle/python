"""Modules to determine number properties"""
def even_or_odd(x):
    """Determines if number is even or odd
    Args:
        x: input integer
    Returns:
        Prints 'Even' or 'Odd'
    """
    if x % 2 == 0:
        print("even")
        return
    print("odd")

def banner(message, border='*'):
    """ Display a banner with border
    Args:
        message: Message to display
        border: outline of message, default value = '*'
    """
    line = len(message) * border
    print(line)
    print(message)
    print(line)


def add_spam(menu = None):
    """Add spam to your breakfast
    :param: menu
    :return: updated breakfast list
    """
    if menu is None:
        menu = []

    menu.append("spam")
    return menu


def main():
    """ Test case for an even and odd numbers"""
    print("7 is:", end='')
    even_or_odd(7)
    print("8 is:", end='')
    even_or_odd(8)


if __name__ == "__main__":
    main()


