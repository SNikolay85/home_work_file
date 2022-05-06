import os, pprint

def read_recipes(file_path):
    #file_path = os.path.join(os.getcwd(), 'recipes.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        cook_book = {}
        while True:
            try:
                all_contains = []
                name_cook = file.readline().strip()
                num_ingredients = int(file.readline().strip())
                for i in range(num_ingredients):
                    list_ingredient = file.readline().strip().split('|')
                    contain_ingredients = {'ingredient_name': list_ingredient[0], 'quantity': list_ingredient[1], 'measure': list_ingredient[2]}
                    all_contains.append(contain_ingredients)
                    cook_book[name_cook] = all_contains
                file.readline()
            except ValueError:
                break
    #pprint.pprint(cook_book, width=100, sort_dicts=False) для первой задачи
    return cook_book

#read_recipes('recipes.txt') для первой задачи

cook_book = read_recipes('recipes.txt')

def get_shop_list_by_dishes(dishes, person_count):
    new = {}
    for name in cook_book.keys():
        if name in dishes:
            for d in cook_book[name]:
                if d['ingredient_name'] not in new.keys():
                    new.setdefault(d['ingredient_name'], {'measure':d['measure'], 'quantity': person_count*int(d['quantity'])})
                else:
                    for a in new[d['ingredient_name']].items():
                        s = a   # промежуточное действие, заполняющее выполнение цикла
                    new[d['ingredient_name']] = {'measure': d['measure'], 'quantity': a[1] + (person_count * int(d['quantity']))}
    pprint.pprint(new, width=100, sort_dicts=False)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3)




