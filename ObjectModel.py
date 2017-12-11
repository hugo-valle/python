"""
Object Model test scripts
"""


def modify(k):
    """
    Modifies the content of my list
    :param k: list
    :return: nothing
    """
    k.append(33)
    print("k= ", k)


def replace(g):
    """
    Replace the content of the list
    :param g: list object
    :return: nothing
    """
    g = [17, 36, 22, 33]
    print("g = ", g)


def update_info(g):
    """
    Updates list content by incrementing each member by 1
    :param g: list object
    :return: nothing
    """
    # g[0] += 1
    # g[1] += 1
    # g[2] += 1
    # g[3] += 1
    i = 0
    while i < len(g):
        g[i] += 1
        i += 1
    print("g = ", g)


def banner(message, border='*'):
    """
    Displays message surrounded by border
    :param message: message <string>
    :param border: border style <char>. Optional with
            default value of '*'
    :return: nothing
    """
    # Take into account border + space on both ends
    line = border * (len(message) + 4)
    print(line)
    print(border, message, border)
    print(line)


def main():
    """
    Dummy testing function
    """
    # m = [9, 12, 45]
    # print("Before m= ", m)
    # modify(m)
    # print("After m= ", m)
    # replace(m)
    # print("After Replace m= ", m)
    # update_info(m)
    # print("After update m= ", m)

    # Set parameters in order
    banner('Real Madrid', '%')
    # Use only required parameters
    banner('WSU')
    # use parameters by name
    banner(border="@", message="Weber State")

    # When are default arguments evaluated??

# Always use immutable objects such as integer
# or strings for default values
def add_spam(menu=None):
    """
    Add spam to my list
    :param menu: Optional list object
    :return: menu
    """
    if menu is None:
        menu = []
    menu.append("spam")
    return menu


def number_info():
    """
    A function that prompts the user
    for two integers, then it prints: The sum,
    the difference, the product, the average,
    and the distance(absolute value), the maximum,
    the minimum
    :return:
    """
    i1 = int(input("Enter an integer: "))
    i2 = int(input("Enter another integer: "))
    print("%-12s%5d" % ("Sum:", i1 + i2))
    print("%-12s%5d" % ("Difference:", i1 - i2))
    print("%-12s%5d" % ("Product:", i1 * i2))
    print("%-12s%8.2f" % ("Average:", (i1 + i2)/2))
    print("%-12s%8.2f" % ("Distance:", abs(i1 - i2)))
    print("%-12s%5d" % ("Max:", max(i1, i2)))
    print("%-12s%5d" % ("Min:", min(i1, i2)))



if __name__ == '__main__':
    #main();
    number_info()