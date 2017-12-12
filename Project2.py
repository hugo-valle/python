from webbrowser import open as openw
import time


def my_break(break_info = None):
    """
    Function to keep track of breaks
    :param break_info: a dictionary with the following keys:
        t_break <int> default is 3
        url <string> default "https://youtu.be/uSD4vsh1zDA"
        t_sleep <int> in seconds, default = 1 hours
    :return:
    """
    if break_info is None:
        # Default info
        break_info = {}
        break_info["t_breaks"] = 3
        break_info["url"] = "https://youtu.be/uSD4vsh1zDA"
        break_info["t_sleep"] = 60 * 60 # one hours
        # TODO: test for individual keys
        # if <key> in dict

    break_count = 0
    while(break_count < break_info['t_breaks']):
        time.sleep(break_info['t_sleep'])
        openw(break_info['url'])
        break_count += 1


if __name__ == '__main__':
    info = {}
    #my_break(info)
    my_break()
