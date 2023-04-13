import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
# from scipy import stats

chat_id = 341395919 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
#     z_score, p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='larger')
#     return p_value < 0.1
    _,p_value = proportions_ztest([x_success,y_success],[x_cnt,y_cnt], alternative = 'smaller')
    if p_value > 0.1:
        return False
    else:
        return True 
