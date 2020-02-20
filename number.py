# -*- coding: utf-8 -*-
import numpy as np

def game_core_v1(number):
    '''Просто угадываем на random ни как не используя информацию о больше или меньше.
       Функция Принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1, 100) # предполагаемое число
        if number == predict: 
            break
    return(count) # выход из цикла, если угадали
        
def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,100)
    predict = 50
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали

def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = 50
    min = 0
    max = 101
    
    
    while number != predict:
        count+=1
        if number > predict: 
            min = predict +  1
            predict = int(predict*1.5) +1
            if predict >max:
                predict = max
        elif number < predict: 
            max = predict -1
            predict //=2
            if predict <min:
                predict = min
        if count > 102:
            return(count)
    return(count) # выход из цикла, если угадали
    
def score_game(game_core_v):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 100, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
#score_game(game_core_v1)
#score_game(game_core_v2)
score_game(game_core_v3)
