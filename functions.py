import os
import shutil
import json


def print_menu():
    print(1, '- Cоздать папку')
    print(2, '- Удалить (файл/папку)')
    print(3, '- Копировать (файл/папку)')
    print(4, '- Просмотр содержимого рабочей директории')
    print(5, '- Сохранить содержимое рабочей директории в файл')
    print(6, '- Файлы рабочей директории')
    print(7, '- Папки рабочей директории')
    print(8, '- Просмотр информации об операционной системе')
    print(9, '- Создатель программы')
    print(10, '- Играть в викторину')
    print(11, '- Мой банковский счет')
    print(12, '- Смена рабочей директории')
    print(0, '- Выход')


def create_dir():
    answer = input('Введите название новой папки: ')
    print('Папка уже существует') if os.path.exists(answer) else os.mkdir(answer)


def delete_dir():
    try:
        answer = input('Введите название удаляемой папки/файла: ')
        os.removedirs(answer) if os.path.isdir(answer) else os.remove(answer)
    except FileNotFoundError:
        print('Папка/файл не найдена')


def copy_dir():
    try:
        first_answer = input('Введите название копируемой папки/файла: ')
        second_answer = input('Введите название новой папки/файла: ')
        shutil.copytree(first_answer, second_answer) if os.path.isdir(first_answer) \
            else shutil.copy(first_answer, second_answer)
    except FileNotFoundError:
        print('Папка/файл не найдена')


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


def save_dir():
    dir_dict = {'files': [file for file in os.listdir('.') if os.path.isfile(file)],
                'dirs': [file for file in os.listdir('.') if os.path.isdir(file)]}
    with open('listdir.txt', 'w') as f:
        json.dump(dir_dict, f)
    return dir_dict
