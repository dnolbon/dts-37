import numpy as np


def game_core_v3(number):
    """
    поиск нужного числа методом деления пополам. Устанавливаем нижнюю и верхнюю границу, далее, если число не угадано,
    то сдвигаем нижнюю или верхнюю границу и повторяем процедуру.
    """
    count = 1

    min_number = 0
    max_number = 100

    def next_number(prev_number):
        numbers_sum = min_number + max_number
        if numbers_sum % 2 == 0:  # проверка на четность
            result = numbers_sum / 2
        else:
            result = (numbers_sum // 2)  # при делении нечтного выбираем меньшее

        if result == prev_number:  # на случай если остались два соседних числа, проверяем меньшее, затем большее
            result += 1

        return result

    predict = next_number(0)

    while number != predict:
        count += 1

        predict = next_number(predict)

        if number > predict:  # если число больше нужного, то сдвигаем нижнюю границу
            min_number = predict
        elif number < predict:  # если число меньше нужного, то сдвигаем верхнюю границу
            max_number = predict

    return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v3)
