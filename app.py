import random


SORT_TYPES = {
    '1': 'bubble',
    '2': 'selection'
}

SIZE = 50

def generate_data(size=SIZE):
    return random.sample(range(1, size + 1), size)

class SortVisualizer:
    def __init__(self, size=SIZE):
        self.size = size
        self.arr = generate_data(size)


def select_choice(sort_types):
    choice = input('выберите вариант сортировки для визуализации(1-2):')
    if choice in sort_types:
        pass
    else:
        print("неверно, выберите из диапазона 1-2")
        select_choice(sort_types)

if __name__ == '__main__':
    print('возможные варианты сортировки:')
    print('1 пузырьковая')
    print('2 выбором')

select_choice(SORT_TYPES)