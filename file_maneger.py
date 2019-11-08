import functions
import os
import platform
import victory
import use_functions

while True:
    functions.print_menu()  # выводим список меню

    choice = input('Выберете номер пункта меню: ')
    if choice == '1':
        functions.create_dir()  # создаем папку

    elif choice == '2':
        functions.delete_dir()  # удаляем папку

    elif choice == '3':
        functions.copy_dir()   # копируем папку

    elif choice == '4':
        print('Содержимое рабочей директории:')
        print(os.listdir('.'))  # папки и файлы рабочей дирректории

    elif choice == '5':
        functions.list_file()  # файлы рабочей дирректории

    elif choice == '6':
        functions.list_folders()  # папки рабочей дирректории

    elif choice == '7':
        print('Информация об ОС:')
        print(platform.uname())   # информация об ОС

    elif choice == '8':
        print('Создатель программы: Шаров Игорь')   # автор программы

    elif choice == '9':    # викторина
        print('Викторина')
        victory.victory()

    elif choice == '10':    # банковский счет
        print('Мой банковский счет. Меню:')
        use_functions.banks()

    elif choice == '11':
        functions.change_dir()  # смена рабочей дирректории

    elif choice == '0':
        print('Вы вышли из программы')
        break

