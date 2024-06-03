import flet as ft  # Добавляем библиотеку flet
import pandas as pd  # Добавляем библиотеку pandas


def main(page: ft.Page):  # Функция работы приложения
    register_username = ft.TextField(label='Введите здесь своё имя', width=700)  # Переменная для имени пользователя при регистрации
    register_password = ft.TextField(label='Введите здесь свой пароль', width=700)  # Переменная для пароля пользователя при регистрации
    register_password_check = ft.TextField(label='Введите свой пароль повторно', width=700)  # Переменная для проверочного пароля при регистрации
    auth_username = ft.TextField(label='Введите здесь своё имя', width=700)  # Переменная для имени пользователя при входе в аккаунт
    auth_password = ft.TextField(label='Введите здесь свой пароль', width=700)  # Переменная для пароля пользователя при входе в аккаунт
    pizza_choice = ft.Dropdown(
        width=600,
        options=[
            ft.dropdown.Option('Маргарита'),
            ft.dropdown.Option('Сицилийская'),
            ft.dropdown.Option('Пепперони'),
            ft.dropdown.Option('С морепродуктами'),
            ft.dropdown.Option('Гавайская'),
            ft.dropdown.Option('Грибная'),
        ],
        hint_text='Выберите пиццу',
    )  # Переменная для выбора пиццы
    pizza_size = ft.Dropdown(
        width=250,
        options=[
            ft.dropdown.Option('24 см'),
            ft.dropdown.Option('30 см'),
            ft.dropdown.Option('40 см'),
        ],
        hint_text='Выберите размер пиццы',
    )  # Переменная для размера пиццы
    menu = ft.Text('                                       Меню пиццы:\n'
                   '\n'
                   '             Пицца                      24 см              30 см             40 см\n'
                   '         Маргарита             500 рублей    550 рублей    600 рублей\n'
                   '       Сицилийская          470 рублей    520 рублей    570 рублей\n'
                   '         Пепперони            360 рублей    400 рублей    450 рублей\n'
                   '  С морепродуктами    450 рублей    500 рублей    550 рублей\n'
                   '          Гавайская            420 рублей    470 рублей    510 рублей\n'
                   '            Грибная              400 рублей    440 рублей    485 рублей\n'
                   '\n'
                   '                        Меню дополнительных блюд:\n'
                   '\n'
                   '                   Блюдо                                         Цена\n'
                   '                   Кетчуп                                    50 рублей\n'
                   '                 Майонез                                  50 рублей\n'
                   '       Чай чёрный, 250 мл                        100 рублей\n'
                   '       Чай зелёный, 250 мл                      100 рублей\n'
                   '          Кока-Кола, 0.5 л                            130 рублей\n'
                   '            Картофель фри                           170 рублей\n'
                   '\n'
                   'Теперь предлагаем вам сделать ваш заказ, нажав кнопку ниже.')  # Переменная для меню
    pizza_price = ft.Text('')  # Переменная для стоимости пиццы
    adding = ft.Dropdown(
        width=250,
        options=[
            ft.dropdown.Option('Кетчуп'),
            ft.dropdown.Option('Майонез'),
            ft.dropdown.Option('Чай чёрный, 250 мл'),
            ft.dropdown.Option('Чай зелёный, 250 мл'),
            ft.dropdown.Option('Кока-Кола, 0.5 л'),
            ft.dropdown.Option('Картофель фри'),
            ft.dropdown.Option('Ничего'),
        ],
    )  # Переменная для добавочного блюда
    adding_price = ft.Text('')  # Переменная для цены добавочного блюда
    summary_price = ft.Text('')  # Переменная для общей цены заказа
    adress_of_payer = ft.TextField(label='Введите здесь свой адрес', width=500)  # Переменная для адреса заказывающего

    def start(e):  # Функция стартового экрана при запуске приложения
        page.clean()
        page.add(
            ft.Text('Здравствуйте, пользователь! Прежде чем начать пользоваться нашим приложением, зайдите в свой аккаунт.\n'
                    'Если у вас нет аккаунта, вы можете его создать, нажав кнопку "Создать аккаунт".\n'
                    'Если аккаунт уже существует, вы можете войти в него, нажав кнопку "Войти в аккаунт".'),
        )
        page.add(ft.Row(controls=[ft.ElevatedButton('Создать аккаунт', on_click=register), ft.ElevatedButton('Войти в аккаунт', on_click=auth)]))  # Кнопки для регистрации или входа в аккаунт
        page.update

    def register(e):  # Функция регистрации нового пользователя
        page.clean()
        register_username.value = ''
        register_password.value = ''
        register_password_check.value = ''  # Анулирование значений переменных для многоразового использования
        page.add(
            ft.Text('Чтобы создать новый аккаунт, введите своё имя пользователя и пароль в отведённые ячейки.\n'
                    'Пароль обязательно должен содержать хотя бы одну букву, иначе система не сможет впоследствии считать его.'),
            register_username,  # Имя пользователя
            register_password,  # Пароль пользователя
            register_password_check,  # Проверочный пароль
            ft.ElevatedButton('Сохранить аккаунт', on_click=register_check)  # Кнопка для проверки данных регистрации
        )
        page.update

    def register_check(e):  # Функция для проверки данных регистрации
        if register_password.value == register_password_check.value:
            users = pd.read_csv('DataFrame.csv')  # Переменная для таблицы с информацией обо всех пользователях
            new_user = pd.DataFrame({'Name': [register_username.value], 'Password': [register_password.value]})  # Переменная для таблицы с информацией о новом пользователе
            users = pd.concat([users, new_user], ignore_index=True)  # Совмещение двух таблиц в одну общую
            users.to_csv('DataFrame.csv', index=False)  # Перевод таблицы из переменой в csv файл
            page.add(
                ft.Text('Аккаунт успешно зарегистрирован! Теперь вы можете войти в него, нажав кнопку ниже.'),  # Если пароли при регистрации совпали
                ft.ElevatedButton('Войти в аккаунт', on_click=auth)  # Кнопка для входа в аккаунт
            )
        else:
            page.add(
                ft.Text('Извините, но ваши пароли не совпадают. Попробуйте ещё раз.'),  # Если пароли при регистрации не совпали
                ft.ElevatedButton('Пройти регистрацию снова', on_click=register)  # Кнопка для повторной регистрации
            )
        page.update

    def auth(e):  # Функция для входа в аккаунт
        page.clean()
        auth_username.value = ''
        auth_password.value = ''  # Анулирование значений переменных для многоразового использования
        page.add(
            ft.Text('Чтобы войти в аккаунт, введите в поля ниже свои имя пользователя и пароль.'),
            auth_username,  # Имя пользователя
            auth_password,  # Пароль пользователя
            ft.ElevatedButton('Войти в аккаунт', on_click=auth_check)  # Кнопка для проверки началия аккаунта с такими данными
        )
        page.update

    def auth_check(e):  # Функция для проверки наличия аккаунта с текущими данными
        users = pd.read_csv('DataFrame.csv')  # Переменная для таблицы с информацией обо всех пользователях
        account_enter = False  # Индикатор наличия аккаунта
        for i in range(len(users)):
            username_check = users['Name'].iloc[i]
            password_check = users['Password'].iloc[i]
            if auth_username.value == username_check and auth_password.value == password_check:
                page.add(
                    ft.Text('Вы успешно зашли в свой аккаунт!'),  # Если аккаунт существует
                    ft.ElevatedButton('Перейти к заказу пиццы', on_click=main_page)  # Кнопка для перехода в главное меню
                )
                account_enter = True
                break
        if not account_enter:
            page.add(
                ft.Text('Скорее всего, вы ошиблись с именем или паролем, либо такого аккаунта не существует.'),  # Если аккаунт не существует
                ft.ElevatedButton('Попробовать ещё раз', on_click=auth)  # Кнопка для повторного входа в аккаунт
            )
        page.update

    def main_page(e):  # Функция старта приложения
        page.clean()
        page.add(
            ft.Text(f'Здравствуйте, {auth_username.value}! Вы зашли в программу для заказа пиццы.'),
            ft.Text('Чтобы сделать свой заказ, нажмите на кнопку "Сделать новый заказ".'),
            ft.Text('Чтобы просмотреть меню нашего сервиса, нажмите кнопку "Показать меню".')  # Приветственные слова
        )
        page.add(ft.Row(controls=[ft.ElevatedButton('Сделать новый заказ', on_click=new_pizza), ft.ElevatedButton('Показать меню', on_click=menu_func)]))  # Кнопки для вывода меню или создания заказа
        page.update

    def menu_func(e):  # Функция вывода меню
        page.clean()
        page.add(
            menu,  # Меню
            ft.ElevatedButton('Сделать новый заказ', on_click=new_pizza)  # Кнопка для создания нового заказа
        )

    def new_pizza(e):  # Функция для добавления пиццы в заказе
        page.clean()
        pizza_choice.value = ''
        pizza_size.value = ''  # Анулирование значений переменных для многоразового использования
        page.add(
            ft.Text('Выберите в выпадающем списке рядом пиццу, которую хотите заказать, и её размер.'),
            pizza_choice,  # Пицца
            pizza_size,  # Размер пиццы
            ft.ElevatedButton('Сохранить пиццу', on_click=addings),  # Кнопка для сохранения пиццы и начала заказа добавочного блюда
        )
        page.update

    def addings(e):  # Функция для добавления добавочных блюд
        adding.value = ''  # Анулирование значения переменной для многоразового использования
        page.add(
            ft.Text('Выберите в выпадающем списке рядом добавочное блюдо.'),
            adding,  # Добавочное блюдо
            ft.ElevatedButton('Сохранить добавочное блюдо', on_click=order_agreeing)  # Кнопка для сохранения доп. блюда и вывода заказа
        )
        page.update

    def order_agreeing(e):  # Функция для вывода заказа
        page.clean()
        if pizza_choice.value == 'Маргарита' and pizza_size.value == '24 cм':
            pizza_price.value = 500
        elif pizza_choice.value == 'Маргарита' and pizza_size.value == '30 см':
            pizza_price.value = 550
        elif pizza_choice.value == 'Маргарита' and pizza_size.value == '40 см':
            pizza_price.value = 600
        elif pizza_choice.value == 'Сицилийская' and pizza_size.value == '24 cм':
            pizza_price.value = 470
        elif pizza_choice.value == 'Сицилийская' and pizza_size.value == '30 см':
            pizza_price.value = 520
        elif pizza_choice.value == 'Сицилийская' and pizza_size.value == '40 см':
            pizza_price.value = 570
        elif pizza_choice.value == 'Пепперони' and pizza_size.value == '24 cм':
            pizza_price.value = 360
        elif pizza_choice.value == 'Пепперони' and pizza_size.value == '30 см':
            pizza_price.value = 400
        elif pizza_choice.value == 'Пепперони' and pizza_size.value == '40 см':
            pizza_price.value = 450
        elif pizza_choice.value == 'С морепродуктами' and pizza_size.value == '24 cм':
            pizza_price.value = 450
        elif pizza_choice.value == 'С морепродуктами' and pizza_size.value == '30 см':
            pizza_price.value = 500
        elif pizza_choice.value == 'С морепродуктами' and pizza_size.value == '40 см':
            pizza_price.value = 550
        elif pizza_choice.value == 'Гавайская' and pizza_size.value == '24 cм':
            pizza_price.value = 420
        elif pizza_choice.value == 'Гавайская' and pizza_size.value == '30 см':
            pizza_price.value = 470
        elif pizza_choice.value == 'Гавайская' and pizza_size.value == '40 см':
            pizza_price.value = 510
        elif pizza_choice.value == 'Грибная' and pizza_size.value == '24 cм':
            pizza_price.value = 400
        elif pizza_choice.value == 'Грибная' and pizza_size.value == '30 см':
            pizza_price.value = 440
        elif pizza_choice.value == 'Грибная' and pizza_size.value == '40 см':
            pizza_price.value = 485  # Обозначение стоимости пиццы в зависимости от её вида и размеров
        if adding.value == 'Кетчуп' or adding.value == 'Майонез':
            adding_price.value = 50
        elif adding.value == 'Чай чёрный, 250 мл' or adding.value == 'Чай зелёный, 250 мл':
            adding_price.value = 100
        elif adding.value == 'Кока-Кола, 0.5 л':
            adding_price.value = 130
        elif adding.value == 'Картофель фри':
            adding_price.value = 170
        elif adding.value == 'Ничего':
            adding_price.value = 0  # Обозначение стоимости доп. блюда в зависимости от его вида
        page.add(
            ft.Text(f"Заказ сохранён! Заказанная пицца: {pizza_choice.value}, размер: {pizza_size.value}, стоимоть пиццы: {pizza_price.value} рублей.")
        )  # Вывод заказа пиццы
        if adding.value != 'Ничего':  # Проверка, есть ли добавочное блюдо
            summary_price.value = pizza_price.value + adding_price.value  # Считаем общую цену заказа
            page.add(
                ft.Text(f"Выбранное дополнительное блюдо к пицце: {adding.value}, стоимость дополнительного блюда: {adding_price.value} рублей.")
            )  # Вывод заказа доп. блюда
        else:
            summary_price.value = pizza_price.value  # Считаем общую цену заказа
        page.add(
                ft.Text(f"Общая стоимость заказа: {summary_price.value} рублей."),  # Вывод общей стоимости заказа
                ft.ElevatedButton('Выбрать место доставки', on_click=adress)  # Кнопка для ввода адреса заказывающего
        )
        page.update

    def adress(e):  # Функция для добавления адреса заказывающего и сохранения информации о заказе
        adress_of_payer.value = ''  # Анулирование значения переменной для многоразового использования
        orders = pd.read_csv('OrderDataFrame.csv')  # Переменная для таблицы со всеми заказами
        new_order = pd.DataFrame({'Username': [auth_username.value], 'Pizza': [pizza_choice.value],
                                  'Pizza_size': [pizza_size.value], 'Adding': [adding.value],
                                  'Summary_price': [summary_price.value]})  # Переменная для таблицы с информацией о текущем заказе
        orders = pd.concat([orders, new_order], ignore_index=True)  # Совмещение двух таблиц в одну общую
        orders.to_csv('OrderDataFrame.csv', index=False)  # Перевод таблицы из переменой в csv файл
        page.add(
            adress_of_payer,  # Адрес
            ft.ElevatedButton('Сохранить адрес', on_click=end_screen)  # Кнопка для вывода общей информации о заказе
        )
        page.update

    def end_screen(e):  # Функция для вывода общей информации о заказе
        page.clean()
        page.add(
            ft.Text(f"Ваш заказ общей стоимостью {summary_price.value} рублей будет доставлен по адресу {adress_of_payer.value} примерно через 40 минут."),  # Вывод общей цены и адреса
            ft.Text('Чтобы сделать новый заказ, вы можете выйти из своего аккаунта, нажав на кнопку ниже.\n'
                    'Спасибо за использование нашего сервиса!'),
            ft.ElevatedButton('Выйти из аккаунта', on_click=start)  # Кнопка для выхода из аккаунта и переноса на страницу с выбором регистрации или входа в аккаунт
        )
        page.update

    page.add(
        ft.ElevatedButton('Запустить приложение', on_click=start)  # Кнопка для запуска приложения
    )
    page.update


ft.app(target=main, view=ft.AppView.WEB_BROWSER)  # Обозначение, что приложение откроется в браузере
