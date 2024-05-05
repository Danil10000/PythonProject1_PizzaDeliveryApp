import flet as ft


def main(page: ft.Page):
    greetings1 = ft.Text('Здравствуйте, пользователь! Вы зашли в программу для заказа пиццы.')
    greetings2 = ft.Text('Чтобы сделать свой заказ, нажмите на кнопку ниже.')
    pizza_choice = ft.Dropdown(
        width=600,
        options=[
            ft.dropdown.Option('Маргарита'),
            ft.dropdown.Option('Сицилийская'),
            ft.dropdown.Option('Пеперони'),
            ft.dropdown.Option('С морепродуктами'),
            ft.dropdown.Option('Гавайская'),
            ft.dropdown.Option('Грибная'),
        ],
    )
    pizza_price = ft.Text('')
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
            ft.Text('Выберите в выпадающем списке рядом пиццу, которую хотите заказать'),
            pizza_choice,
            ft.ElevatedButton('Сохранить заказ', on_click=pizza_deliv),
        )
        page.update

    def pizza_deliv(e):
        if pizza_choice.value == 'Маргарита':
            pizza_price.value = 550
        elif pizza_choice.value == 'Сицилийская':
            pizza_price.value = 520
        elif pizza_choice.value == 'Пеперони':
            pizza_price.value = 400
        elif pizza_choice.value == 'С морепродуктами':
            pizza_price.value = 500
        elif pizza_choice.value == 'Гавайская':
            pizza_price.value = 470
        elif pizza_choice.value == 'Грибная':
            pizza_price.value = 440
        page.add(
            ft.Text(f"Заказ сохранён! Заказанная пицца: {pizza_choice.value}, стоимоть: {pizza_price.value} рублей."),
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
        page.add(
            ft.Text(f"Пицца {pizza_choice.value} стоимостью {pizza_price.value} рублей будет доставлена по адресу {adress_of_payer.value} примерно через 40 минут."),
            ft.Text('Если хотите сделать новый заказ, перезапустите приложение, многоразовые заказы пока в разработке. Спасибо за использование нашего сервиса!')
        )
        page.update

    page.add(
        ft.ElevatedButton('Запустить приложение', on_click=start)
    )
    page.update

ft.app(target=main, view=ft.AppView.WEB_BROWSER)