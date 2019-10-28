def banks():

    account = 0

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. выход')

        choice = input('Выберите пункт меню:')
        if choice == '1':
            payment = float(input('Введите сумму пополнения счета:'))
            account += payment
            print('Баланс счета:', account)

        elif choice == '2':
            price_product = float(input('Введите стоимость покупки:'))
            if price_product > account:
                print('На счете не достаточно средств')
            else:
                account -= price_product
                print('Баланс счета:', account)

        elif choice == '3':
            print('До свидания')
            break
        else:
            print('Неверный пункт меню!')
