'''Визуализатор алгоритмов сортировки.
'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

INTERVAL_VIZUALIZATION = 1  # задать интервал между кадрами визуализации

SORT_TYPES = {
    '1': 'bubble',
    '2': 'selection'
}

SIZE = 30  # задать количество элементов в массиве


def generate_data(size=SIZE):
    '''Генерирует массив уникальных чисел заданного размера.'''
    return random.sample(range(1, size + 1), size)


class SortVisualizer:
    '''Для визуализации алгоритмов сортировки.'''

    def __init__(self, size=SIZE):
        '''Инициализирует визуализатор.'''
        self.size = size
        self.arr = generate_data(size)
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.bars = self.ax.bar(range(len(self.arr)), self.arr, color='skyblue')
        self.ax.set_title('Визуализация сортировки')
        self.ax.set_xlim(0, size)
        self.generator = None

    def bubble_sort_gen(self):
        '''Генератор алгоритма пузырьковой сортировки.'''
        arr = self.arr.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                yield arr, {j: 'red', j+1: 'orange'}
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    yield arr, {j: 'green', j+1: 'green'}

    def selection_sort_gen(self):
        '''Генератор алгоритма сортировки выбором.'''
        arr = self.arr.copy()
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                yield arr, {i: 'blue', j: 'red', min_idx: 'orange'}
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            yield arr, {i: 'green', min_idx: 'green'}

    def animate(self, sort_type='bubble'):
        '''Анимация выбранного алгоритма сортировки.'''    
        sort_methods = {
            'bubble': self.bubble_sort_gen,
            'selection': self.selection_sort_gen
        }

        if sort_type in sort_methods:
            self.generator = sort_methods[sort_type]()
        else:
            print('Неизвестный тип сортировки')
            return

        def update(frame):
            '''Покадровое обновление графика.'''
            try:
                arr, highlights = next(self.generator)
                for i, (bar, height) in enumerate(zip(self.bars, arr)):
                    bar.set_height(height)
                    if i in highlights:
                        bar.set_color(highlights[i])
                    else:
                        bar.set_color('skyblue')
            except StopIteration:
                for bar in self.bars:
                    bar.set_color('lightgreen')
                self.ani.event_source.stop()
            return self.bars

        self.ani = animation.FuncAnimation(
            self.fig,
            update,
            interval=INTERVAL_VIZUALIZATION,
            blit=False,
            repeat=False,
            cache_frame_data=False
        )
        plt.show()


def select_choice(sort_types):
    '''Запрос у пользователя алгоритма сортировки для визуализации.'''
    choice = input('выберите вариант сортировки для визуализации(1-2):')
    if choice in sort_types:
        return choice
    else:
        print("неверно, выберите из диапазона 1-2")
        return select_choice(sort_types)


if __name__ == '__main__':
    visualizer = SortVisualizer()
    print('возможные варианты сортировки:')
    print('1 пузырьковая')
    print('2 выбором')

visualizer.animate(SORT_TYPES[select_choice(SORT_TYPES)])
