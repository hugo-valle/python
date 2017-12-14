import sys
from itertools import count, islice

def sequence():
    """
    Recaman series: a_0 = 0,
    a_n=a_(n-1) - n. If the result is positive
            and not already in the list.
    Otherwise: a_n = a_(n-1) + n
    :return:
    """
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n # a_n = a_(n-1) + n
        #a_n=a_(n-1) - n. If the result is positive
        #and not already in the list.
        if c < 0 or c in seen:
            c = a + n
        a = c


def write_sequence(filename, num):
    """
    Write Recaman's sequence to a text file
    :param filename: file name to create
    :param num: maximum number to write
    :return: nothing
    """
    f = open(filename, mode='wt', encoding='utf-8')
    # write info
    f.writelines("{0}\n".format(r)
                 for r in islice(sequence(), num+1))
    f.close()


def read_series(filename):
    """
    Read Recaman series from file. Creates a list of
    each record on the file
    :param filename:
    :return: list with file records
    """
    pass


def main():
    f = "recamanSeries.txt"
    n = 100
    write_sequence(f, n)


if __name__ == '__main__':
    main()