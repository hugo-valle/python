import os


def get_files(dir):
    file_list = os.listdir(dir)

    print(file_list)


def main():
    data_dir = r"C:\Users\hugovalle1\Desktop\PythonIntro\python\data"
    get_files(data_dir)


if __name__ == '__main__':
    main()