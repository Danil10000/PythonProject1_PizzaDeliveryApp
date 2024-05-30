import flet as ft # Добавляем библиотеку flet


def main(page: ft.Page):
    greetings1 = ft.Text('Здравствуйте, пользователь! Вы зашли в программу для заказа пиццы.')
    greetings2 = ft.Text('Чтобы сделать свой заказ, нажмите на кнопку "Сделать новый заказ".')
    greetings3 = ft.Text('Чтобы просмотреть меню нашего сервиса, нажмите кнопку "Показать меню".') # Приветственные слова
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
    ) # Переменная для выбора пиццы
    pizza_size = ft.Dropdown(
        width=250,
        options=[
            ft.dropdown.Option('24 см'),
            ft.dropdown.Option('30 см'),
            ft.dropdown.Option('40 см'),
        ],
        hint_text='Выберите размер пиццы',
    ) # Переменная для размера пиццы
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
                   'Теперь предлагаем вам сделать ваш заказ, нажав кнопку ниже.') # Переменная для меню
    pizza_price = ft.Text('') # Переменная для стоимости пиццы
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
    ) # Переменная для добавочного блюда
    adding_price = ft.Text('') # Переменная для цены добавочного блюда
    summary_price = ft.Text('') # Переменная для общей цены заказа
    adress_of_payer = ft.TextField(label='Введите здесь свой адрес', width=500) # Переменная для адреса заказывающего

    def start(e): # Функция старта приложения
        page.clean()
        page.add(
            greetings1,
            greetings2,
            greetings3
        )
        page.add(ft.Row(controls=[ft.ElevatedButton('Сделать новый заказ', on_click=new_pizza), ft.ElevatedButton('Показать меню', on_click=menu_func)])) # Кнопки для вывода меню или создания заказа
        page.update

    def menu_func(e): # Функция вывода меню
        page.clean()
        page.add(
            menu, # Меню
            ft.ElevatedButton('Сделать новый заказ', on_click=new_pizza) # Кнопка для создания нового заказа
        )

    def new_pizza(e): # Функция для добавления пиццы в заказе
        page.clean()
        page.add(
            ft.Text('Выберите в выпадающем списке рядом пиццу, которую хотите заказать, и её размер.'),
            pizza_choice, # Пицца
            pizza_size, # Размер пиццы
            ft.ElevatedButton('Сохранить пиццу', on_click=addings), # Кнопка для сохранения пиццы и начала заказа добавочного блюда
        )
        page.update

    def addings(e): # Функция для добавления добавочных блюд
        page.add(
            ft.Text('Выберите в выпадающем списке рядом добавочное блюдо.'),
            adding, # Добавочное блюдо
            ft.ElevatedButton('Сохранить добавочное блюдо', on_click=pizza_agreeing) # Кнопка для сохранения доп. блюда и вывода заказа
        )
        page.update

    def pizza_agreeing(e): # Функция для вывода заказа
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
            pizza_price.value = 485 # Вводим стоимость пиццы в зависимости от её вида и размеров
        if adding.value == 'Кетчуп' or adding.value == 'Майонез':
            adding_price.value = 50
        elif adding.value == 'Чай чёрный, 250 мл' or adding.value == 'Чай зелёный, 250 мл':
            adding_price.value = 100
        elif adding.value == 'Кока-Кола, 0.5 л':
            adding_price.value = 130
        elif adding.value == 'Картофель фри':
            adding_price.value = 170 # Вводим стоимость доп. блюда в зависимости от его вида
        page.add(
            ft.Text(f"Заказ сохранён! Заказанная пицца: {pizza_choice.value}, размер: {pizza_size.value}, стоимоть пиццы: {pizza_price.value} рублей.")
        ) # Вывод заказа пиццы
        if adding.value != 'Ничего': # Проверка, есть ли добавочное блюдо
            summary_price.value = pizza_price.value + adding_price.value # Считаем общую цену заказа
            page.add(
                ft.Text(f"Выбранное дополнительное блюдо к пицце: {adding.value}, стоимость дополнительного блюда: {adding_price.value} рублей.")
            ) # Вывод заказа доп. блюда
        else:
            summary_price.value = pizza_price.value # Считаем общую цену заказа
        page.add(
                ft.Text(f"Общая стоимость заказа: {summary_price.value} рублей."),
                ft.ElevatedButton('Выбрать место доставки', on_click=adress) # Кнопка для ввода адреса заказывающего
        )
        page.update

    def adress(e): # Функция для добавления адреса заказывающего
        page.add(
            adress_of_payer, # Адрес
            ft.ElevatedButton('Сохранить адрес', on_click=end_screen) # Кнопка для вывода общей информации о заказе
        )
        page.update

    def end_screen(e): # Функция для вывода общей информации о заказе
        page.clean()
        page.add(
            ft.Text(f"Ваш заказ общей стоимостью {summary_price.value} рублей будет доставлен по адресу {adress_of_payer.value} примерно через 40 минут."), # Вывод общей цены и адреса
            ft.Text('Если хотите сделать новый заказ, перезапустите приложение, множественные заказы пока в разработке. Спасибо за использование нашего сервиса!')
        )
        page.update

    page.add(
        ft.ElevatedButton('Запустить приложение', on_click=start) # Кнопка для запуска приложения
    )
    page.update


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
