def swap(val):
    """
    Swap the first half with the second half
    of the list
    :param val: a list of objects
    :return: new order list
    """
    m = len(val)//2
    # TODO: make sure it works for odd
    # number of elements
    return val[m:] + val[:m]


def main():
    val = [9, 13, 21, 4, 11, 7, 1, 3]
    print(val)
    val = swap(val)
    print(val)


if __name__ == '__main__':
    main()