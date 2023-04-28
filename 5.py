import os
import re


SEARCH_NAME = "filenames"
FOLDER_NAME = "test"
EMAIL_REG = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

path_list = list()
counter_ = [0]
email_set = set()


def task1(path_folder: str) -> None:
    '''
    Функция считает количество файлов имеющих в названии "filenames".
    И добавляет в path_list полный путь до каждого имеющегося файла в директории FOLDER_NAME
    '''
    list_dirs = os.listdir(path_folder)
    for name_file in list_dirs:
        new_path_to_file = os.path.join(path_folder, name_file)
        if os.path.isdir(new_path_to_file):
            task1(new_path_to_file)
        else:
            # добавим полный путь до каждого файла, для использования в task2()
            path_list.append(new_path_to_file)
            if SEARCH_NAME in name_file:
                counter_[0] += 1


def task2() -> None:
    '''
    Функция ищет в каждой строке каждого файла в
    директории FOLDER_NAME любые емейлы
    '''
    for path_file in path_list:
        if os.stat(path_file).st_size != 0:
            with open(path_file, "r") as file:
                line = file.readline()
                while line:
                    if emails := re.findall(EMAIL_REG, line):
                        email_set.update(emails)
                    line = file.readline()


def main():
    task1(os.path.join(os.getcwd(), FOLDER_NAME))
    task2()
    print('\nКоличество файлов содержащих строку "filenames" в названии: {}'.format(*counter_))
    print(f"Не повторяющиеся емейлы: {email_set}\n")


if __name__ == "__main__":
    main()
