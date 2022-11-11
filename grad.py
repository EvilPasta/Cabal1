import numpy as np

def coefCount(y_train): # Функция для нахождения параетров a и b, где y это ln(исх данн)
    x_train = list(range(1, len(y_train)+1))

    # Задаем начальные случайные значения коэфицентом линейной регрессии
    a = np.random.randn(1)
    b = np.random.randn(1)

    stepSize = 0.000346  # Скорость обучения
    stepCount = 100000   # Количество проходов

    for _ in range(stepCount):
        y_hat = a + b * x_train   # Рассчитываем результирующий массив с текущими коэффициента a и b на основе обучающей выборки
        error = (y_train - y_hat) # Считаем отклонение нового резутьтата от обучающего

        # Cчитаем градиенты
        a_grad = -2 * error.mean()             # Для коэф a
        b_grad = -2 * (x_train * error).mean() # Для коэф a

        # Обновляем параметры используя коэф скорости обучения
        a = a - stepSize * a_grad
        b = b - stepSize * b_grad
    print('a_gr: ', a[0])
    print('b_gr: ', b[0])
