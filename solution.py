import pandas as pd
import numpy as np


chat_id = 1188007817 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    alpha = 1 - p
    chi_sq = np.sum(x**2, axis=1) / (37 * np.var(x))
    chi_left = chi2.ppf(q=alpha/2, df=1)
    chi_right = chi2.ppf(q=1-alpha/2, df=1)
    sigma_left = np.sqrt(np.sum(x**2) / (37 * chi_right))
    sigma_right = np.sqrt(np.sum(x**2) / (37 * chi_left))
    list1 = [sigma_left, sigma_right]
    return list1

