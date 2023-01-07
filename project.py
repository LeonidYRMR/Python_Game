from gameclasses import BinaryGame, MathGame
from gametasks import print_instructions, get_user_score, update_user_score

try:
    math_instructions = ("\nВ этой игре вам предлагается решить простую арифметическую задачу. "
                         "\nЗа каждый правильный ответ вам начисляется одно очко. "
                         "\nЗа ошибочные ответы очки не вычитаются \n")
    binary_instructions = ("\nВ этой игре вы получаете десятичное число."
                           "\nВаша задача преобразовать его в двоичную систему счисления."
                           "\nЗа каждый правильный ответ вам начисляется одно очко. "
                           "\nЗа ошибочные ответы очки не вычитаются \n")

    mg = MathGame()
    bg = BinaryGame()

    user_name = input("Пожалуйста введите ваше имя: ")
    score = int(get_user_score(user_name))
    if score == -1:
        new_user = True
        score = 0
    else:
        new_user = False

    print(f"\nПриветствую {user_name}, добро пожаловать в игру!")
    print(f"\nТвой текущий счёт: {score}")

    user_choice = 0

    while user_choice != '-1':
        game = input("\nВыбери игру: Math Game (1) или Binary Game (2) ")

        while game != '1' and game != '2':
            print("\nВы ввели неверный вариант. Пожалуйста попробуйте еще.\n")
            game = input("Выбери игру: Math Game (1) или Binary Game (2)")

        num_promt = input("\nКакое кол-во вопросов выберете? (от 1 до 10) ")

        while True:
            try:
                num = int(num_promt)
                break
            except:
                print("Не действительно число.")
                print('Попробуйте снова:')
                num_promt = input("\nКакое кол-во вопросов выберете? (от 1 до 10)")

        if game == '1':
            mg.no_of_questions = num
            print_instructions(math_instructions)
            score += mg.generate_questions()
        else:
            bg.no_of_questions = num
            print_instructions(binary_instructions)
            score += bg.generate_questions()

        print(f"Твой текущий счет: {score}\n")
        user_choice = input('Нажми "Enter" чтобы продолжить или введи "-1" чтобы завершить: ')

    update_user_score(new_user, user_name, str(score))

except Exception as e:
    print("An unknown error occured. Program will exit.")
    print("Error: ", e)
