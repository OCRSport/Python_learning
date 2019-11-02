import os
import shutil


def print_menu():
    print(1, '- Cоздать папку')
    print(2, '- Удалить (файл/папку)')
    print(3, '- Копировать (файл/папку)')
    print(4, '- Просмотр содержимого рабочей директории')
    print(5, '- Файлы рабочей директории')
    print(6, '- Папки рабочей директории')
    print(7, '- Просмотр информации об операционной системе')
    print(8, '- Создатель программы')
    print(9, '- Играть в викторину')
    print(10, '- Мой банковский счет')
    print(11, '- Смена рабочей директории')
    print(0, '- Выход')


def create_dir():
    while True:
        answer = input('Введите название новой папки: ')
        if os.path.exists(answer):
            print('Папка уже существует')
        else:
            os.mkdir(answer)
            break


def delete_dir():
    answer = input('Введите название удаляемой папки/файла: ')
    if os.path.isdir(answer):
        os.removedirs(answer)
    else:
        os.remove(answer)


def copy_dir():
    first_answer = input('Введите название копируемой папки/файла: ')
    second_answer = input('Введите название новой папки/файла: ')
    if os.path.isdir(first_answer):
        shutil.copytree(first_answer, second_answer)
    else:
        shutil.copy(first_answer, second_answer)


def list_file():
    print('Список файлов директории:')
    print(list(filter(lambda x: os.path.isfile(x), os.listdir("."))))


def list_folders():
    print('Список папок директории:')
    print(list(filter(lambda x: os.path.isdir(x), os.listdir("."))))


def change_dir():
    print('Текущая директория:', os.getcwd())
    new_dir = input('Укажите путь к новой директории:')
    os.chdir(new_dir)
    print('Новая директория:', os.getcwd())

