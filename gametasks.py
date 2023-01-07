from os import remove, rename


def print_instructions(instructions):
    print(instructions)


def get_user_score(user_name):
    try:
        entry = open('UserScores.txt', 'r')
        for line in entry:
            content = line.split(', ')
            if content[0] == user_name:
                entry.close()
                return content[1]
            entry.close()
            return '-1'

    except IOError:
        print('Игрок не найден. Новый Игрок был создан.')
        entry = open('UserScores.txt', 'w')
        entry.close()
        return '-1'


def update_user_score(new_user, user_name, score):
    if new_user:
        entry = open('UserScores.txt', 'a')
        entry.write(user_name + ', ' + score + '\n')
        entry.close()
    else:
        temp = open('userScores.tmp', 'w')
        entry = open('userScores.tmp', 'r')
        for line in entry:
            content = line.split(', ')
            if content[0] == user_name:
                temp.write(user_name + ', ' + score + '\n')
            else:
                temp.write(line)
        entry.close()
        temp.close()

        remove('UserScores.txt')
        rename('UserScores.tmp', 'UserScores.txt')
