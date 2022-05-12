# -*- coding: cp1251 -*-
def get_item(file):
    key = file.__next__().strip('\n')
    n = int(file.__next__().strip())
    lst = []
    lt = []
    dic = {}
    a = 0
    for i in range(n):
        lt += file.__next__().strip('\n').split('|')
        dic = {'ingredient_name': lt[i + a], 'quantity': lt[i + a + 1], 'measure': lt[i + a + 2]}
        a += 2
        lst.append(dic)
    return key, lst

def restaurant_menu():
    cook_book = {}
    with open('task.txt') as file:
        while True:
            try:
                key, lst = get_item(file)
                cook_book[key] = lst
                next(file)
            except StopIteration:
                break
        file.close
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    get_shop_list = {}
    cook_book = restaurant_menu()
    for i in dishes:
        a = 0
        for ii in cook_book[i]:
            get_shop_list[cook_book[i][a]['ingredient_name']] = {'measure': cook_book[i][a]['measure'], 'quantity': int(cook_book[i][a]['quantity']) * person_count}
            a += 1
    print(get_shop_list)
            
def get_shop():
    dishes = []
    person_count = int(input('Введите колличество персон: '))
    while True:
        dish = input('Введите блюда, для подтверждения введите q: ').capitalize()
        if dish == 'Q':
            break
        dishes.append(dish)
    # dishes = ['Омлет', 'Утка по-пекински']
    # person_count = 2
    get_shop_list_by_dishes(dishes, person_count)
get_shop()
