import pandas as pd
import numpy as np
import math
# chat_id = 1119567869 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = np.full(x.shape, 86) # создаем массив t, заполненный 86
    lt = x.sum() # находим сумму всех ламп в поставках
    l = lt / t.mean() # оцениваем параметр L, используя формулу Lt/t
    return l # возвращаем оценку параметра L
