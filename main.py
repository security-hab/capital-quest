import random
import time

import schedule

balance: float = 500
assets = {
    'stocks': {'APPL': 0, 'TSLA': 0}, # Stocks amount, that user have in the game
    'crypto': {'BTC': 0, 'ETH': 0},
    'real_estate': {'Apartments': False, 'House': False}
}

stock_prices = {
    'APPL': 150,
    'TSLA': 600,
}

def buy_stock(stock_name, amount):
    global balance
    stock_price = stock_prices[stock_name]
    total_price = stock_price * amount

    if balance >= total_price:
        balance -= total_price
        assets['stocks'][stock_name] += amount
        print(f'Вы купили {amount} шт. акции {stock_name} по цене {stock_price}$\nВаш текущий баланс составляет: {float(balance)}$')
    else:
        print('Недостаточно средств на балансе!')

def sell_stock(stock_name, amount):
    global balance
    stock_price = stock_prices[stock_name]
    if assets['stocks'][stock_name] >= amount:
        balance += stock_price * amount
        assets['stocks'][stock_name] -= amount
        print(f'Вы продали акцию {stock_name} по цене {stock_price}$')
    else:
        print('У вас недостаточно акций!')

def updating_price():
    global stock_prices
    for stock_name, current_price in stock_prices.items():
        new_price = current_price + random.randint(-10, 10)
        stock_prices[stock_name] = new_price
        print(f'Цена акции {stock_name} изменилась на {new_price}$')

def user_interaction():
    while True:
        print('\nВыберите действие:')
        print('1. Купить акции')
        print('2. Продать акции')
        print('3. Посмотреть текущий баланс')
        print('4. Выйти из игры')

        action = int(input('Ваш выбор: '))

        if action == 1:
            stock_name = input('Введите название акции: ')
            amount = int(input('Введите количество акций: '))
            buy_stock(stock_name, amount)
        elif action == 2:
            stock_name = input('Введите название акции: ')
            amount = int(input('Введите количество акций: '))
            sell_stock(stock_name, amount)
        elif action == 3:
            print(f'Текущий баланс: {balance}$')
        elif action == 4:
            print('Вы вышли из игры.')
            break
        else:
            print('Неверный ввод! Попробуйте еще раз.')

schedule.every(3).seconds.do(updating_price)

if __name__ == '__main__':
    while True:
        user_interaction()
        schedule.run_pending()
        time.sleep(1)
