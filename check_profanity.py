import urllib.request
import urllib.parse


def read_text():
    with open("movie_quotes.txt", mode='rt', encoding='utf-8') as f:
        for line in f:
            # Call check profanity
            if check_profanity(line.strip()):
                print("Profanity Alert")
            else:
                print('This line in document has no curse words')


def check_profanity(text_to_check):
    """
    Check profanity words from a text file
    Connect to:
    "http://wdylike.appspot.com/?q="
    to check for profanity
    :param text_to_check: text to check
    :return: True or False
    """
    url_api = "http://wdylike.appspot.com/?q="
    # open connection
    conn = urllib.request.urlopen(url_api +
                            urllib.parse.quote(text_to_check))
    # read info
    out = conn.read()
    #print(out.decode('utf-8'))
    if out.decode('utf-8') == "false":
        return False
    else:
        return True

if __name__ == '__main__':
   read_text()