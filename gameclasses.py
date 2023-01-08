from random import randint


class Game:
    # Инициализация переменной no_of_questions (кол-во вопросов)
    # Для использования в дочерних классах
    def __init__(self, no_of_questions=0):
        self._no_of_questions = no_of_questions

    @property
    def no_of_questions(self):
        return self._no_of_questions

    @no_of_questions.setter
    # Свойство для установки пользователем ограниченного количество вопросов в игре (1-10)
    def no_of_questions(self, value):
        if value < 1:
            self._no_of_questions = 1
            print('\nМинимально кол-во вопросов = 1')
            print('Значит будешь отвечать на 1 вопрос)\n')
        elif value > 10:
            self._no_of_questions = 10
            print('\nМаксимальное кол-во вопросов = 10')
            print('Значит будешь отвечать на 10 вопросов)\n')
        else:
            self._no_of_questions = value


class BinaryGame(Game):
    # Генерация вопросов
    def generate_questions(self):
        # Счет игрока
        score = 0
        # no_of_questions кол-во вопросов выбранных игроком
        for i in range(self.no_of_questions):
            # Генерация случайного числа от 1 до 100
            binary = randint(1, 100)
            user_result = input(f'\nПожалуйста преобразуйте число {binary} в двоичную систему счисления: ')

            while True:
                try:
                    # Проверка ответа игрока
                    answer = int(user_result, base=2)
                    if answer == binary:
                        print('Отлично!')
                        score += 1
                        break
                    else:
                        print(f"Неверный ответ. Правильный ответ - {bin(binary)[2:]}.\n")
                        break
                # Отлов недопустимого ввода
                except:
                    print("НЕВЕРНО, ты ввел не бинарное число... Пожалуйста попробуйте снова: ")
                    user_result = input(f'\nПожалуйста преобразуйте число {binary} в двоичную систему счисления: ')

        return score


class MathGame(Game):
    # Генерация вопросов
    def generate_questions(self):
        score = 0
        number_list = [0, 0, 0, 0, 0]
        symbol_list = ['', '', '', '']
        operator_dict = {
            1: ' + ',
            2: ' - ',
            3: '*',
            4: '**',
        }
        # no_of_questions кол-во вопросов выбранных игроком
        for i in range(self.no_of_questions):
            # Заполнение списка случайными числами от 1 до 9
            for j in (0, 4):
                number_list[j] = randint(1, 9)
            # Заполнение списка случайными символами (недопустимо заполнение степени(**) подряд)
            for k in (0, 3):
                if k > 0 and symbol_list[k - 1] == '**':
                    symbol_list[k] = operator_dict[randint(1, 3)]
                else:
                    symbol_list[k] = operator_dict[randint(1, 4)]
            # Запись строчного математического выражения
            question_string = str(number_list[0])
            for q in (0, 3):
                question_string += str(symbol_list[q]) + str(number_list[q+1])
            # Вычисление выражения и замена символа возведения в степень
            result = eval(question_string)
            question_string = question_string.replace('**', '^')

            user_result = input(f"Вычисли значение выражения: {question_string}\n")

            while True:
                try:
                    # Проверка ответа игрока
                    if user_result == str(result):
                        print('Правильный ответ!')
                        score += 1
                        break
                    else:
                        print(f"Ответ неверный =( \nПравильный ответ: {result}.\n")
                        break
                # Отлов недопустимого ввода
                except:
                    print("Вы ввели неправильное значение. \nПожалуйста попробуйте снова: \n")
                    user_result = int(input(f"Вычисли значение выражения: {question_string}\n"))

        return score
