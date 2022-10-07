
class contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


def print_user(bd, i):
    string = ''
    string = 'ID = ' + str(i+1) + '\n'
    string += bd[1][i]
    if bd[2][i] != 'Нет':
        string += " " + bd[2][i]
    if bd[3][i] != 'Нет':
        string += " " + bd[3][i]
    string += '\n'
    if bd[4][i] != 'Нет':
        string += "Номер телефона: " + bd[4][i] + '\n'
    if bd[5][i] != 'Нет':
        string += "Почта: " + bd[5][i]
    print(string)
    print()













print("Введите название файла")
f = open(input(), encoding='utf-8')
bd = [[], [], [], [], [], []]
id = 1
for s in f:
    new_info = s.split(",")
    new_info[1] = new_info[1].replace(" ", "")
    new_info[2] = new_info[2].replace(" ", "")
    new_info[2] = new_info[2].replace("\n", "")
    user = contact(new_info[0], new_info[1], new_info[2])
    bd[0].append(id)
    id+=1
    name = user.name.split(" ")
    while len(name) < 3:
        name.append('Нет')
    for i in range(0, 3):
        bd[i+1].append(name[i])
    if user.phone != '':
        bd[4].append(user.phone)
    else:
        bd[4].append('Нет')
    if user.email != '':
        bd[5].append(user.email)
    else:
        bd[5].append('Нет')
print("Список команд: ", "1 - Показать список контактов", "2 - Поиск",
    "3 - Показать контакты без данных", "4 - Изменение контакта",
    "5 - Завершить программу", sep="\n")
c = int(input())
while c != "qwerty":
    if c == 1:
        for i in range(0, id-1):
            string = ''
            string = 'ID = ' + str(bd[0][i]) + '\n'
            string += bd[1][i]
            if bd[2][i] != 'Нет':
                string += " " + bd[2][i]
            if bd[3][i] != 'Нет':
                string += " " + bd[3][i]
            string += '\n'
            if bd[4][i] != 'Нет':
                string += "Номер телефона: " + bd[4][i] + '\n'
            if bd[5][i] != 'Нет':
                string += "Почта: " + bd[5][i]
            print(string)
            print()
        print("Список команд: ", "1 - Показать список контактов", "2 - Поиск",
              "3 - Показать контакты без данных", "4 - Изменение контакта",
              "5 - Завершить программу", sep="\n")
        c = int(input())
    elif c == 2:
        print("По чему вы хотите искать?", "1 - по телефону", "2 - по почте", "3 - по имени", sep='\n')
        c2 = int(input())
        if c2 == 1:
            print("Введите номер телефона.")
            search_phone = input()
            flag = False
            for i in range(0, len(bd[0])):
                if bd[4][i] == search_phone:
                    print_user(bd, i)
                    flag = True
            if not flag:
                print("Такого контакта нет")
        if c2 == 2:
            print("Введите номер почту.")
            search_email = input()
            flag = False
            for i in range(0, len(bd[0])):
                if bd[5][i] == search_email:
                    print_user(bd, i)
                    flag = True
            if not flag:
                print("Такого контакта нет")
        if c2 == 3:
            print('Как вы хотите искать?')
            print('1 - по имени',
                  '2 - по фамилии',
                  '3 - по отчеству',
                  '4 - по имени и фамилии',
                  '5 - по имени и отчеству',
                  '6 - по фамилии и отчеству',
                  '7 - по имени, фамилии и отчеству',
                  sep='\n'
                  )
            c3 = int(input())
            if c3 == 1:
                print("Введите имя.")
                search_name = input()
                flag = False
                for i in range(0, len(bd[0])):
                    if bd[2][i] == search_name:
                        print_user(bd, i)
                        flag = True
                if not flag:
                    print("Такого контакта нет")
            if c3 == 2:
                print("Введите имя.")
                search_name = input()
                flag = False
                for i in range(0, len(bd[0])):
                    if bd[1][i] == search_name:
                        print_user(bd, i)
                        flag = True
                if not flag:
                    print("Такого контакта нет")
            if c3 == 3:
                print("Введите отчество")
                search_name = input()
                flag = False
                for i in range(0, len(bd[0])):
                    if bd[3][i] == search_name:
                        print_user(bd, i)
                        flag = True
                if not flag:
                    print("Такого контакта нет")
            if c3 == 4:
                print('Введите имя и фамилию через пробел')
                search_name = input()
                search_name = search_name.split(' ')
                flag = False
                for i in range(0, len(bd[0])):
                    if bd[2][i] == search_name[0] and bd[1][i] == search_name[1]:
                        print_user(bd, i)
                        flag = True
                if not flag:
                    print("Такого контакта нет")
            if c3 == 5:
                print('Введите имя и отчество через пробел')
                search_name = input()
                search_name = search_name.split(' ')
                flag = False
                for i in range(0, len(bd[0])):
                    if bd[2][i] == search_name[0] and bd[3][i] == search_name[1]:
                        print_user(bd, i)
                        flag = True
                if not flag:
                    print("Такого контакта нет")
            if c3 == 6:
                print('Введите фамилию и отчество через пробел')
                search_name = input()
                search_name = search_name.split(' ')
                flag = False
                for i in range(0, len(bd[0])):
                    if bd[1][i] == search_name[0] and bd[3][i] == search_name[1]:
                        print_user(bd, i)
                        flag = True
                if not flag:
                    print("Такого контакта нет")
            if c3 == 7:
                print('Введите имя, фамилию и отчество через пробел')
                search_name = input()
                search_name = search_name.split(' ')
                flag = False
                for i in range(0, len(bd[0])):
                    if bd[2][i] == search_name[0] and bd[1][i] == search_name[1] and bd[3][i] == search_name[2]:
                        print_user(bd, i)
                        flag = True
                if not flag:
                    print("Такого контакта нет")
        print("Список команд: ", "1 - Показать список контактов", "2 - Поиск",
              "3 - Показать контакты без данных", "4 - Изменение контакта",
              "5 - Завершить программу", sep="\n")
        c = int(input())
    elif c == 3:
        print("Показать:", "1 - без номера", "2 - без почты", "3 - без обоих", sep="\n")
        c4 = int(input())
        flag = False
        if c4 == 1:
            for i in range(0, id-1):
                if bd[4][i] == "Нет":
                    print_user(bd, i)
                    flag = True
        if c4 == 2:
            for i in range(0, id-1):
                if bd[5][i] == "Нет":
                    print_user(bd, i)
                    flag = True
        if c4 == 3:
            for i in range(0, id-1):
                if bd[4][i] == "Нет" and bd[5][i] == "Нет":
                    print_user(bd, i)
                    flag = True
        if not flag:
            print("Такого контакта нет")
        print("Список команд: ", "1 - Показать список контактов", "2 - Поиск",
              "3 - Показать контакты без данных", "4 - Изменение контакта",
              "5 - Завершить программу", sep="\n")
        c = int(input())
    elif c == 4:
        print("Режим изменения контакта", "Введите ID", sep='\n')
        id_ = int(input())
        id_ -=1
        print("Вы хотите изменить данные контакта:")
        print_user(bd, id_)
        print("Что вы хотите изменить?", '1 - ФИО', '2 - номер', '3 - почту', sep='\n')
        c5 = int(input())
        if c5 == 1:
            print('Введите фамилию, имя и отчество через пробел')
            change = input()
            change = change.split(' ')
            bd[1][id_] = change[0]
            bd[2][id_] = change[1]
            bd[3][id_] = change[2]
        if c5 == 2:
            print('Введите номер')
            change = input()
            bd[4][id_] = change
        if c5 == 3:
            print('Введите почту')
            change = input()
            bd[5][id_] = change
        print("Данные изменены:")
        print_user(bd, id_)
        print("Список команд: ", "1 - Показать список контактов", "2 - Поиск",
              "3 - Показать контакты без данных", "4 - Изменение контакта",
              "5 - Завершить программу", sep="\n")
        c = int(input())
    elif c == 5:
        print("Программа выключена")
        break
