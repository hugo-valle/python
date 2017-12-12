count = 0  # global

def show_count():
    print(count)


def set_count(c):
    global count
    count = c

