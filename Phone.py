from csv import DictReader, DictWriter
from os.path import exists


class NameError(Exception):
    def _init_(self, txt):
        self.txt = txt


def get_info():
    flag = False
    while not flag:
        try:

            first_name = input("Имя: ")
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя")
            second_name = input("Фамилия: ")
            if len(second_name) < 5:
                raise NameError("Слишком короткая фамилия")
            phone_nomber = input("Телефон: ")
            if len(phone_nomber) < 11:
                raise NameError("Слишком короткий номер")

        except NameError as err:
            print(err)
        else:
            flag = True

    return [first_name, second_name, phone_nomber]


def create_file(file_name):
    with open(file_name, "w", encoding="utf-8", newline="") as data:
        f_w = DictWriter(data, fieldnames=["first name", "second name", "phone number"])
        f_w.writeheader()


def write_file(file_name):
    user_data = get_info()
    res = read_file(file_name)
    new_obj = {"first name": user_data[0], "second name": user_data[1], "phone number": user_data[2]}
    res.append(new_obj)
    standart_write(file_name, res)


def read_file(file_name):
    with open(file_name, encoding="utf-8") as data:
        f_r = DictReader(data)
        return list(f_r)


def remowe_row(file_name):
    search = int(input("введите номер строки для удаления: "))
    res = read_file(file_name)
    if search <= len(res):
        res.pop(search - 1)
        standart_write(file_name, res)
    else:
        print("введен неверный номер строки")


def standart_write(file_name, res):
    with open(file_name, "w", encoding="utf-8", newline="") as data:
        f_w = DictWriter(data, fieldnames=["first name", "second name", "phone number"])
        f_w.writeheader()
        f_w.writerows(res)


def copy_data(file_name, file_name_1):
    create_file(file_name_1)
    res = read_file(file_name)
    standart_write(file_name_1, res)
def copy_row(file_name):

    search = int(input("введите номер строки для копирования: "))
    res = read_file(file_name)
    res_2 = read_file(file_name_2)
    if search <= len(res):

        res_2.append(res[search-1])
        standart_write(file_name_2, res_2)
    else:
        print("введен неверный номер строки")

file_name = "phone.csv"
file_name_1 = "phone_copy.csv"
file_name_2 = "phone_copy_row.csv"

def main():
    while True:
        command = input(" введите команду: ")
        if command == "q":
            break
        elif command == "w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == "r":
            if not exists(file_name):
                print("файл отсутствует")
                continue
            print(*read_file(file_name))
        elif command == "d":
            if not exists(file_name):
                print("файл отсутствует")
                continue
            remowe_row(file_name)
        elif command == "c":
            if not exists(file_name):
                print("файл для копирования отсутствует")
                continue
            copy_data(file_name, file_name_1)
        elif command == "cr":
            if not exists(file_name_2):
                create_file(file_name_2)
            copy_row(file_name)


main()
