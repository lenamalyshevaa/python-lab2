def main():
    items_str = input('Введите список товаров через запятую: ')
    items = items_str.split(',')
    stores = []
    stores_prices = {}

    while True:
       store = input('Введите название магазина (или стоп): ').strip()
       if store.lower() == 'стоп':
           break
       stores.append(store)
       stores_prices[store] = {}
       
       for item in items:
           price = float(input(f'Введите стоимость товара {item} в магазине {store}: '))
           stores_prices[store][item] = price

    min_price, min_store = None, None
    for store in stores:
        print(f'Магазин {store}:')
        store_sum = 0
        for item, price in stores_prices[store].items():
            print(f'* {item} = {price} руб.')
            store_sum += price
        if (min_price is None) or (store_sum < min_price):
            min_price, min_store = store_sum, store
    if min_store is not None:
        print(f'На набор товаров минимальная цена в магазине {min_store} - {min_price} руб.')
    else:
        print(f'Ошибка, минимальная цена не найдена')

if __name__=='__main__':
    main()    
