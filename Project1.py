#!/usr/bin/env python
"""Retrieve and print words from URL
Usage Windows:
    python day1.py <URL>
Usage Linux:
    python3 day1.py <URL>
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.
    Args:
        url: The URL of a UTF-8 text document
    Returns:
        A list of strings containing the words from
        the document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            words = line.decode('utf-8').split()
            for word in words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line
     Args:
         An iterable series of printable items
    """
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
  main(sys.argv[1])
  # Test file
  #main("http://sixty-north.com/c/t.txt")