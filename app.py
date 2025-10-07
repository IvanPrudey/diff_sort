import matplotlib.pyplot as plt
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
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.bars = self.ax.bar(range(len(self.arr)), self.arr, color='skyblue')
        self.ax.set_title('Визуализация сортировки')
        self.ax.set_xlim(0, size)
        self.generator = None
    

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