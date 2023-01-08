from gameclasses import BinaryGame, MathGame
from gametasks import print_instructions, get_user_score, update_user_score

try:
    # Инструкции к играм
    math_instructions = ("\nВ этой игре вам предлагается решить простую арифметическую задачу. "
                         "\nЗа каждый правильный ответ вам начисляется одно очко. "
                         "\nЗа ошибочные ответы очки не вычитаются \n")
    binary_instructions = ("\nВ этой игре вы получаете десятичное число."
                           "\nВаша задача преобразовать его в двоичную систему счисления."
                           "\nЗа каждый правильный ответ вам начисляется одно очко. "
                           "\nЗа ошибочные ответы очки не вычитаются \n")
    # Сокращение
    mg = MathGame()
    bg = BinaryGame()
    # Начало
    user_name = input("Пожалуйста введите ваше имя: ")
    # Получение счета игрока
    score = int(get_user_score(user_name))
    # Проверка нового игрока
    if score == -1:
        new_user = True
        score = 0
    else:
        new_user = False

    print(f"\nПриветствую {user_name}, добро пожаловать в игру!")
    print(f"\nТвой текущий счёт: {score}")

    user_choice = 0
    # -1 для завершения игры
    while user_choice != '-1':
        # Выбор игры
        game = input("\nВыбери игру: Math Game (1) или Binary Game (2) ")

        while game != '1' and game != '2':
            print("\nВы ввели неверный вариант. Пожалуйста попробуйте еще.\n")
            game = input("Выбери игру: Math Game (1) или Binary Game (2)")

        num_promt = input("\nКакое кол-во вопросов выберете? (от 1 до 10) ")
        # Проверка ввода на число
        while True:
            try:
                num = int(num_promt)
                break
            except:
                print("Не допустимое значение.")
                print('Попробуйте снова:')
                num_promt = input("\nКакое кол-во вопросов выберете? (от 1 до 10)")
        # Запуск игры Math Game
        if game == '1':
            # Передаем для генерации кол-во вопросов
            mg.no_of_questions = num
            # Выводим инструкцию к игре
            print_instructions(math_instructions)
            # Добавление очков за игру
            score += mg.generate_questions()
        else:
            # Запуск игры Binary Game
            bg.no_of_questions = num
            print_instructions(binary_instructions)
            score += bg.generate_questions()
        # После ответов на все вопросы показать счет и продолжить или завершить игру
        print(f"Твой текущий счет: {score}\n")
        user_choice = input('Нажми "Enter" чтобы продолжить или введи "-1" чтобы завершить: ')
    # Обновление счета игрока
    update_user_score(new_user, user_name, str(score))

except Exception as e:
    print("An unknown error occured. Program will exit.")
    print("Error: ", e)
