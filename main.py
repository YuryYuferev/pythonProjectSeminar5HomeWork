# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# def Del_Word(s):
#     return False if 'абв' in s else True
# print('Введите текст: ')
# a = input()
# a = a.split()
# print(a)
# a = list(filter(Del_Word,a))
# print(a)

# Создайте программу для игры с конфетами человек против человека. На столе лежит 2021 конфета. Играют два игрока, делая ход,  друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import randint
# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
# counter1 = 0
# counter2 = 0
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         print(player2, k, counter2, value)
# if flag:
#     print(f"Поздравляю! В этот раз победил {player1}")
# else:
#     print(f"Поздравляю! В этот раз победил {player2}")

# a) Реализация игры (с конфетами), человек против бота

# from random import randint
# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2)
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
# counter1 = 0
# counter2 = 0
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = randint(1,29)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
# if flag:
#     print(f"Поздравляю! В этот раз победил {player1}")
# else:
#     print(f"Поздравляю! В этот раз победил {player2}")

# Реализация игры (с конфетами), человек против бота c "интеллектом":

# from random import randint
#
# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
# def bot_calc(value):
#     k = randint(1,29)
#     while value-k <= 28 and value > 29:
#         k = randint(1,29)
#     return k
# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2)
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
# counter1 = 0
# counter2 = 0
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = bot_calc(value)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
# if flag:
#     print(f"Поздравляю! В этот раз победил {player1}")
# else:
#     print(f"Поздравляю! В этот раз победил {player2}")

# Создайте программу для игры в "Крестики-нолики".

# def draw_board(board):
#     print("-------------")
#     for i in range(3):
#         print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print("-------------")
#
# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token + "?")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print("Эта клеточка уже занята")
#         else:
#             print("Некорректный ввод. Введите число от 1 до 9.")
# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print(tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# board = list(range(1,10))
# main(board)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# import os
# os.system('cls')
# def encode_file(my_text):
#     str_code = ''
#     count = 1
#     for i in range(len(my_text)):
#         if i < len(my_text)-1:
#             if my_text[i] == my_text[i + 1]:
#                 count += 1
#             else:
#                 str_code += str(count) + my_text[i]
#                 count = 1
#         else:
#             str_code += str(count) + my_text[i]
#     return str_code
# def decode_file(strc):
#     count = ''
#     result = ''
#     for i in strc:
#         if i.isdigit():
#             count += i
#         else:
#             result += i * int(count)
#             count = ''
#     return result
# text = input("Введите текст для кодировки: ")
# print(f'Предоставлен следующий текст: \n{text}')
# with open('task_4_decode.txt', 'w') as data:
#     data.write(text)
# with open('task_4_decode.txt', 'r') as data:
#     my_text = data.read()
# strc = encode_file(my_text)
# print(f'Текст после кодировки: \n{strc}')
# with open('task_4_code.txt', 'w') as data:
#     data.write(strc)
# with open('task_4_code.txt', 'r') as data:
#     my_text = data.read()
# total = decode_file(my_text)
# print(f'Текст после дешифровки: \n{total}')
# with open('task_4_decode.txt', 'w') as data:
#     data.write(total)
