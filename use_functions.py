def banks():

    account = 0
    history = []

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню:')
        if choice == '1':
            payment = int(input('Введите сумму пополнения счета:'))
            account += payment
            print('Баланс счета:', account)

        elif choice == '2':
            price_product = int(input('Введите стоимость покупки:'))
            if price_product > account:
                print('На счете не достаточно средств')
            else:
                product = input('Введите название покупки:')
                account -= price_product
                history.append(f"Товар: {product}; Стоимость: {price_product}")
                print('Баланс счета:', account)

        elif choice == '3':
            print('История покупок:', history)

        elif choice == '4':
            print('До свидания')
            break
        else:
            print('Неверный пункт меню!')
