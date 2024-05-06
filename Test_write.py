import flet as ft


def main(page: ft.Page):
    greetings1 = ft.Text('Здравствуйте, пользователь! Вы зашли в программу для заказа пиццы.')
    greetings2 = ft.Text('Чтобы сделать свой заказ, нажмите на кнопку ниже.')
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
    )
    pizza_size = ft.Dropdown(
        width=150,
        options=[
            ft.dropdown.Option('24 см'),
            ft.dropdown.Option('30 см'),
            ft.dropdown.Option('40 см'),
        ],
        hint_text='Выберите размер пиццы',
    )
    pizza_price = ft.Text('')
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
    )
    adding_price = ft.Text('')
    adress_of_payer = ft.TextField(label='Введите здесь свой адрес', width=500)

    def start(e):
        page.add(
            greetings1,
            greetings2,
            ft.ElevatedButton('Сделать новый заказ', on_click=new_pizza)
        )
        page.update

    def new_pizza(e):
        page.add(
            ft.Text('Выберите в выпадающем списке рядом пиццу, которую хотите заказать, и её размер.'),
            pizza_choice,
            pizza_size,
            ft.ElevatedButton('Сохранить заказ', on_click=addings),
        )
        page.update

    def addings(e):
        page.add(
            ft.Text('Выберите в выпадающем списке рядом добавочное блюдо.'),
            adding,
            ft.ElevatedButton('Сохранить добавочное блюдо', on_click=pizza_agreeing)
        )
        page.update

    def pizza_agreeing(e):
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
            pizza_price.value = 485
        if adding.value == 'Кетчуп' or adding.value == 'Майонез':
            adding_price.value = 50
        elif adding.value == 'Чай чёрный, 250 мл' or adding.value == 'Чай зелёный, 250 мл':
            adding_price.value = 100
        elif adding.value == 'Кока-Кола, 0.5 л':
            adding_price.value = 130
        elif adding.value == 'Картофель фри':
            adding_price.value = 170
        page.add(
            ft.Text(f"Заказ сохранён! Заказанная пицца: {pizza_choice.value}, размер: {pizza_size.value}, стоимоть пиццы: {pizza_price.value} рублей.")
        )
        if adding.value == 'Ничего':
            page.add(
                ft.ElevatedButton('Выбрать место доставки', on_click=adress)
            )
        else:
            page.add(
                ft.Text(f"Выбранное дополнительное блюдо к пицце: {adding.value}, стоимость дополнительного блюда: {adding_price.value} рублей."),
                ft.ElevatedButton('Выбрать место доставки', on_click=adress)
            )
        page.update

    def adress(e):
        page.add(
            adress_of_payer,
            ft.ElevatedButton('Сохранить адрес', on_click=end_screen)
        )
        page.update

    def end_screen(e):
        if adding.value == 'Ничего':
            page.add(
                ft.Text(f"Пицца {pizza_choice.value} стоимостью {pizza_price.value} рублей будет доставлена по адресу {adress_of_payer.value} примерно через 40 минут."),
                ft.Text('Если хотите сделать новый заказ, перезапустите приложение, многоразовые заказы пока в разработке. Спасибо за использование нашего сервиса!')
            )
        else:
            page.add(
                ft.Text(f"Пицца {pizza_choice.value} стоимостью {pizza_price.value} рублей и дополнительное блюдо {adding.value} стоимостью {adding_price.value} рублей будет доставлена по адресу {adress_of_payer.value} примерно через 40 минут."),
                ft.Text('Если хотите сделать новый заказ, перезапустите приложение, многоразовые заказы пока в разработке. Спасибо за использование нашего сервиса!')
            )
        page.update

    page.add(
        ft.ElevatedButton('Запустить приложение', on_click=start)
    )
    page.update

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
