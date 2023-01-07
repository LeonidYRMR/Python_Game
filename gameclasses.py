from random import randint


class Game:
    def __init__(self, no_of_questions=0):
        self._no_of_questions = no_of_questions

    @property
    def no_of_questions(self):
        return self._no_of_questions

    @no_of_questions.setter
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
    def generate_questions(self):
        score = 0
        for i in range(self.no_of_questions):
            base10 = randint(1, 100)
            user_result = input(f'\nПожалуйста преобразуйте число {base10} в двоичную систему счисления: ')

            while True:
                try:
                    answer = bin(base10)[2:]
                    if answer == user_result:
                        print('Отлично!')
                        score += 1
                        break
                    else:
                        print(f"Неверный ответ. Правильный ответ - {answer}.\n")
                        break
                except:
                    print("НЕВЕРНО, ты ввел не бинарное число... Пожалуйста попробуйте снова: ")
                    user_result = input(f'\nПожалуйста преобразуйте число {base10} в двоичную систему счисления: ')

        return score


class MathGame(Game):
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
        for i in range(self.no_of_questions):

            for j in (0, 4):
                number_list[j] = randint(1, 9)

            for k in (0, 3):
                if k > 0 and symbol_list[k - 1] == '**':
                    symbol_list[k] = operator_dict[randint(1, 3)]
                else:
                    symbol_list[k] = operator_dict[randint(1, 4)]

            question_string = str(number_list[0])
            for q in (0, 3):
                question_string += str(symbol_list[q]) + str(number_list[q+1])

            result = eval(question_string)
            question_string = question_string.replace('**', '^')

            user_result = input(f"Вычисли значение выражения: {question_string}\n")

            while True:
                try:
                    if user_result == str(result):
                        print('Правильный ответ!')
                        score += 1
                        break
                    else:
                        print(f"Ответ неверный =( \nПравильный ответ: {result}.\n")
                        break
                except:
                    print("Вы ввели неправильное значение. \nПожалуйста попробуйте снова: \n")
                    user_result = int(input(f"Вычисли значение выражения: {question_string}\n"))

        return score
