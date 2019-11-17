import os
import pickle


def banks():
    account = 0
    orders = []
    if os.path.exists('account.txt'):
        with open('account.txt', 'r') as f:
            account = int(f.read())
    if os.path.exists('orders.txt'):
        with open('orders.txt', 'rb') as func:
            orders = pickle.load(func)

    while True:
        print('1. Пополнить счет')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            try:
                payment = int(input('Введите сумму пополнения счета: '))
                account += payment
                print('Баланс счета:', account)
            except ValueError:
                print('Вы ввели не число')

        elif choice == '2':
            try:
                price_product = int(input('Введите стоимость покупки: '))
                if price_product > account:
                    print('На счете не достаточно средств')
            except ValueError:
                print('Вы ввели не число')
            else:
                name_product = input('Введите название покупки: ')
                account -= price_product
                order = (name_product, price_product)
                orders.append(order)
                print('Баланс счета:', account)

        elif choice == '3':
            for i, order in enumerate(orders):
                print('Покупка №', i+1, ':', order)

        elif choice == '4':
            with open('account.txt', 'w') as f:
                f.write(str(account))
            with open('orders.txt', 'wb') as func:
                pickle.dump(orders, func)
            print('До свидания')
            break
        else:
            print('Неверный пункт меню!')
