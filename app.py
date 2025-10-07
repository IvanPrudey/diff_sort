if __name__ == '__main__':
    print('возможные варианты сортировки:')
    print('1 пузырьковая')
    print('2 выбором')

sort_types = {
    '1': 'bubble',
    '2': 'selection'
}

def select_choice(sort_types):
    choice = input('выберите вариант сортировки для визуализации(1-2):')
    if choice in sort_types:
        pass
    else:
        print("неверный выбор, ")
        select_choice(sort_types)

select_choice(sort_types)