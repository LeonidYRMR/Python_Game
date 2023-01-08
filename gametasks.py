from os import remove, rename

# Вывод инструкций к играм
def print_instructions(instructions):
    print(instructions)

# Получение счета игрока
def get_user_score(user_name):
    try:
        # Если игрок есть в файле - вернуть текущий счет игрока, если нет вернуть -1(новый игрок)
        entry = open('UserScores.txt', 'r')
        for line in entry:
            content = line.split(', ')
            if content[0] == user_name:
                entry.close()
                return content[1]
        entry.close()
        return '-1'

    except IOError:
        # Первое создание файла
        print('Файл не найден. Новый файл был создан.')
        entry = open('UserScores.txt', 'w')
        entry.close()
        return '-1'

# Обновление счета игрока после игры
def update_user_score(new_user, user_name, score):
    if new_user:
        # Если новый игрок, то добавить его имя и счет в конец файла
        entry = open('UserScores.txt', 'a')
        entry.write(user_name + ', ' + score + '\n')
        entry.close()
    else:
        # Если игрок уже существует создать временный файл записать в него все из основного файла и обновить счет данного игрока
        temp = open('userScores.tmp', 'w')
        entry = open('UserScores.txt', 'r')
        for line in entry:
            content = line.split(', ')
            if content[0] == user_name:
                temp.write(user_name + ', ' + score + '\n')
            else:
                temp.write(line)
        entry.close()
        temp.close()
        # Удаляем основной и переименовываем временный обновленный файл в основной
        remove('UserScores.txt')
        rename('userScores.tmp', 'UserScores.txt')
