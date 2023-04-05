import pandas as pd
import numpy as np


chat_id = 1188007817 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    total = sum(x)
    return total / (n*6) # Ваш ответ
