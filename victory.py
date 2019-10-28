import random


def victory():
    writers = dict()
    writers['Пушкин'] = '26.05.1799', 'двадцать шестое мая 1799 года'
    writers['Гоголь'] = '31.03.1809', 'тридцать первое марта 1809 года'
    writers['Блок'] = '28.11.1880', 'двадцать восьмое ноября 1880 года'
    writers['Лермонтов'] = '15.10.1814', 'пятнадцатое октября 1814 года'
    writers['Чехов'] = '29.01.1860', 'двадцать девятое января 1860 года'
    writers['Достоевский'] = '11.11.1821', 'одиннадцатое ноября 1821 года'
    writers['Бунин'] = '22.10.1870', 'двадцать второе ноября 1870 года'
    writers['Тургенев'] = '09.10.1818', 'девятое ноября 1818 года'
    writers['Есенин'] = '03.10.1895', 'третье ноября 1895 года'
    writers['Булгаков'] = '15.09.1891', 'пятнадцатое сентября 1891 года'

    selection = random.sample(writers.keys(), 5)
    while True:
        true_answer = 0
        for i in range(5):
            selection_i = selection[i]
            print('Введите дату рождения (дд.мм.гг)', selection_i, ':')
            answer = str(input())
            if answer == writers[selection_i][0]:
                true_answer += 1
                print('Верно')
            else:
                print("Неверно. Правильный ответ: ", writers[selection_i][1])
        print('Количество правильных ответов: ', true_answer)
        print('Количество ошибок: ', 5 - true_answer)
        new_victory = input('Начать викторину сначала? Да/Нет ')
        if new_victory == 'Нет':
            break
