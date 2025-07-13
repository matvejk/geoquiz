import json
import os


def is_deleted(codes):
    with open('deletedcodes.txt', 'r') as data:
        deleted_codes = json.load(data)
    if int(codes) < 0:
        codes *= -1
        for i in range(len(deleted_codes)):
            if int(deleted_codes[i][0]) == codes:
                return i
    for i in range(len(deleted_codes)):
        if int(deleted_codes[i][0]) == codes:
            return True
    return False


def pdfgen(code, password, tasks):
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    # импорт кириллицы
    pdfmetrics.registerFont(TTFont('Regular', 'Montserrat-Medium.ttf'))
    pdfmetrics.registerFont(TTFont('Bold', 'Montserrat-Bold.ttf'))
    folder_path = 'Lists/' + code
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = 'Lists/' + code + '/' + code + '.pdf'
    pdf_file = canvas.Canvas(filename, pagesize=A4)
    width, height = A4  # x = 595 y = 841

    # позиционирование для считывания
    pdf_file.drawImage("granitsa.png", 50, height - 390)
    pdf_file.drawImage("granitsa.png", 534, height - 390)
    pdf_file.drawImage("granitsa.png", 50, height - 670)
    pdf_file.drawImage("granitsa.png", 534, height - 670)

    # хедэр
    pdf_file.drawImage('logo.png', 100, height - 128 - 32, 128, 128)
    pdf_file.setFont("Regular", 16)
    pdf_file.drawString(250, height - 70 - 30, "География в школе 1502 | Гамма")
    pdf_file.drawString(250, height - 90 - 30, "Осенний географический квиз")
    pdf_file.drawString(250, height - 110 - 30, "ДД.ММ.ГГГГ")
    pdf_file.setFont("Bold", 18)
    pdf_file.drawString(225, height - 180, "ЛИСТ УЧАСТНИКА")

    pdf_file.setFont("Regular", 8)
    pdf_file.drawString(50, height - 200,
                        "0. Не используйте гаджеты и не списывайте у кого-либо. За это соревнование невозможно получить плохую оценку.")
    pdf_file.drawString(50, height - 210,
                        "1. В лист впечатаны буквы. За тридцать секунд до начала соревнования дежурный включит карту для")
    pdf_file.drawString(50, height - 220,
                        "определения позиций букв. Вы можете записывать месторасположения букв на свободном месте (НЕ в рамках!).")
    pdf_file.drawString(50, height - 230,
                        "2. Заносите ответы СТРОГО в предусмотренные рамки. Ответы за рамками проверяться и учитываться НЕ будут.")
    pdf_file.drawString(50, height - 240,
                        "Если Вам не хватило места, зачеркните ответ в основной рамке и пишите в дополнительной.")
    pdf_file.drawString(50, height - 250,
                        "При ответе в дополнительной рамке укажите букву вопроса рядом с ответом. Пишите строго внутри рамок.")
    pdf_file.drawImage("primer.png", 100, height - 305, 400, 50)
    pdf_file.drawString(50, height - 310,
                        "3. Учитывается время выполнения заданий. Самые быстрые 10% получат множитель π/e ≈ 1.16, медленные - e/π ≈ 0.87.")
    pdf_file.drawString(50, height - 320,
                        "При этом не разрешено бегать всегда, где это может быть опасно. Всегда нельзя бегать на лестницах.")
    pdf_file.drawString(50, height - 330,
                        "4. Нормативное время - 10 минут. Все результаты с временем, превышающим это, будут обнулены.")
    pdf_file.drawString(50, height - 340,
                        "5. Проходить по буквам не по порядку разрешается и приветствуется. Используйте время эффективно!")
    pdf_file.setFont("Bold", 8)
    pdf_file.drawString(50, height - 350,
                        "Примите π ≈ 201/64. На Земле примерно 30% суши. Считайте, что суша распределена по Земле практически случайно.")
    pdf_file.setFont("Bold", 16)
    pdf_file.drawString(155, height - 380, f"Лист ответов. Код участника:        {code}")
    pdf_file.rect(440, height - 382, 50, 20, stroke=1, fill=0)

    for i in range(len(tasks)):
        pdf_file.rect(50 + 30, height - 412 - 25 * i, 50, 25, stroke=1, fill=0)
        pdf_file.drawString(65 + 30, height - 410 - 25 * i, f"{tasks[i][0]}")
        pdf_file.rect(100 + 30, height - 412 - 25 * i, 400, 25, stroke=1, fill=0)

    pdf_file.rect(50 + 30, height - 412 - 25 * 5 - 50 - 10, 450, 70, stroke=1, fill=0)

    pdf_file.setFont("Regular", 12)
    pdf_file.drawString(50, height - 412 - 25 * 5 - 50 - 10 - 15 - 10,
                        "Организатор, занеси время выполнения в поле справа:")
    pdf_file.rect(430, height - 412 - 25 * 5 - 50 - 10 - 15 - 12 - 10, 100, 30, stroke=1, fill=0)
    pdf_file.setFont("Regular", 8)
    pdf_file.drawString(50, height - 690, f"Эта часть листа остаётся у участника. После проверки вы сможете")
    pdf_file.drawString(50, height - 700, f"просмотреть свой результат в telegram-боте.")
    pdf_file.drawString(50, height - 710, f"При первом входе в бот введите свой логин: {code}, пароль - {password}.")
    pdf_file.drawString(50, height - 720, f"Для захода в бот перейдите по QR-коду справа или введите")
    pdf_file.drawString(50, height - 730, f"прямую ссылку: t.me/Quiz1502Bot")

    pdf_file.drawImage('tglink.png', 350, height - 820, 150, 150)

    pdf_file.showPage()
    pdf_file.save()

    return True


def encode():
    probely()
    with open('result.txt', 'r') as data:
        res = json.load(data)
    print()
    print('Кодируем новую работу. Введите -1, если желаете вернуться в главное меню, иначе нажмите ENTER')
    code = input()
    if code == '-1':
        return True
    g = len(res)
    code = str(g)
    while len(code) < 3:
        code = '0' + code
    print('Новой работе присвоен код', code)
    spis = ['Не внесено'] * 7
    spis.append('Не посчитано')
    spis.append('Не посчитано')
    spis.append('Не внесено')
    spis.append('Скан не загружен')
    res.append(spis)
    res[int(code)][0] = code
    res[int(code)][1] = input('Введите имя и фамилию в формате Фамилия Имя: ')
    ma = res[int(code)][1].split()
    perem = ma[1] + ma[0][0]
    with open('passwords.txt', 'r') as data:
        passwords = json.load(data)
    passwords.append([code, perem, 0])
    with open('passwords.txt', 'w') as data:
        json.dump(passwords, data)
    res[int(code)][2] = input('Введите класс в формате XXY, где ХХ - номер, Y - буква. Пример: 09Ж ')
    import random
    res[int(code)][4] = []
    global group_1, group_2, group_3, group_4, group_5
    random.shuffle(group_1)
    res[int(code)][4].append(group_1[0])
    random.shuffle(group_2)
    res[int(code)][4].append(group_2[0])
    random.shuffle(group_3)
    res[int(code)][4].append(group_3[0])
    random.shuffle(group_4)
    res[int(code)][4].append(group_4[0])
    random.shuffle(group_5)
    res[int(code)][4].append(group_5[0])
    random.shuffle(res[int(code)][4])
    print(code * 72, sep='')
    bool = pdfgen(code, perem, res[int(code)][4])
    print()
    with open('result.txt', 'w') as data:
        json.dump(res, data)
    print(f'Лист участника сгенерирован под именем {code}.pdf в папке {code}')


def time():
    probely()
    with open('result.txt', 'r') as data:
        res = json.load(data)
    codes = input('Введите код участника. Три цифры без лишних знаков: ')
    try:
        codes = int(codes)
        k = res[codes]
    except:
        print('Что-то пошло не так. Для сохранения данных выхожу из функции')
        return True
    if codes == 0:
        print('Нулевой код? Несмешно.')
        return True
    if is_deleted(codes):
        print('Данный участник был удалён. Внесение времени невозможно.')
        return True
    if res[codes][3] != 'Не внесено':
        print('Время уже внесено. Внести заново? Введите -1, если да')
        if input() != '-1':
            return True
    print('Участник', res[codes][1], 'имеет время', res[codes][3],
          'в секундах. Если участник не тот, повторите предыдущее время')
    tim = input('Введите время в СЕКУНДАХ (если ошиблись и нет пред. времени, введите Не внесено): ')
    try:
        tim = int(tim)
        res[codes][3] = tim
        res[codes][7] = round(1 - (tim - 300) / 150, 3)
        if res[codes][7] > 2.5:
            res[codes][7] = 2.501
        if res[codes][7] < 0.20:
            res[codes][7] = 0.201
        if res[codes][6]!='Не внесено':
            res[codes][8] = round(res[codes][7] * res[codes][6], 1)
        with open('result.txt', 'w') as data:
            json.dump(res, data)
        print('Время внесено. Спасибо')

    except:
        if tim != 'Не внесено':
            print(
                'Попробуйте ещё раз внести время. Если вы ошиблись, введите Не внесено (с учётом регистра и пробелов)')
            time()
            return True


def checkwork():
    probely()
    global login_now
    with open('result.txt', 'r') as data:
        res = json.load(data)
    codes = input('Введите код участника. Три цифры без лишних знаков: ')
    try:
        codes = int(codes)
    except:
        print('Что-то пошло не так. Для сохранения данных выхожу из функции')
        return True
    if is_deleted(codes):
        print('Данный участник был удалён. Внесение времени невозможно.')
        return True
    if res[codes][5] != 'Не внесено':
        print('Эта работа уже проверена. Проверить заново? Введите -1, если да')
        if input() != '-1':
            return True
    if res[codes][3] == 'Не внесено':
        print('Время прохождения маршрута не внесено. Проверка невозможна.')
        return True
    print(
        'Возьмите лист участника. Сравнивайте ответы с эталонными. Когда будете готовы начать проверку, нажмите ENTER')
    print('За ответ начисляется ДО 1 балла.')
    q = input()
    print()
    summa = []
    print('1 вопрос:', res[codes][4][0][1], '. Балл: ')
    summa.append(float(input()))
    print('2 вопрос:', res[codes][4][1][1], '. Балл: ')
    summa.append(float(input()))
    print('3 вопрос:', res[codes][4][2][1], '. Балл: ')
    summa.append(float(input()))
    print('4 вопрос:', res[codes][4][3][1], '. Балл: ')
    summa.append(float(input()))
    print('5 вопрос:', res[codes][4][4][1], '. Балл: ')
    summa.append(float(input()))
    for i in range(len(summa)):
        if int(summa[i]) > 1 or int(summa[i]) < -1:
            print('Вы косячите!')
            return True
    res[codes][5] = summa
    res[codes][6] = round((sum(summa) * 20), 1)
    res[codes][8] = round(res[codes][7] * res[codes][6], 1)
    res[codes][9] = login_now
    with open('result.txt', 'w') as data:
        json.dump(res, data)
    print('Внесение завершено')
    return True


def resultadmins():
    probely()
    with open('result.txt', 'r') as data:
        res = json.load(data)
    print('------------------------------')
    print('Рейтинговая таблица участников на данный момент')
    matrix = []
    codes = []
    matrix2 = []
    for i in range(len(res)):
        perem = ''
        for k in range(5):
            perem += res[i][4][k][0]
            perem += ' '
        if i == 0:
            matrix.append(
                [res[i][0], res[i][1], res[i][2], res[i][3], *res[i][4][0], res[i][6], res[i][7], res[i][8], res[i][9]])
        else:
            if not (is_deleted(i)):
                if res[i][8] == 'Не посчитано':
                    matrix2.append(
                        [res[i][0], res[i][1], res[i][2], res[i][3], perem, res[i][6], res[i][7], res[i][8], res[i][9]])
                else:
                    matrix.append(
                        [res[i][0], res[i][1], res[i][2], res[i][3], perem, res[i][6], res[i][7], res[i][8], res[i][9]])
            else:
                codes.append(i)
    codes.sort()
    matrix1 = []
    for i in codes:
        perem = ''
        for k in range(5):
            perem += res[i][4][k][0]
            perem += ' '
        matrix1.append([res[i][0], res[i][1], res[i][2], res[i][3], perem, res[i][6], res[i][7], res[i][8], res[i][9]])
    while True:
        c = 0
        for i in range(1, len(matrix) - 1):
            if matrix[i][7] < matrix[i + 1][7]:
                c = 1
                (matrix[i + 1], matrix[i]) = (matrix[i], matrix[i + 1])
        if c == 0:
            break
    for i in range(len(matrix1)):
        matrix.append(matrix1[i])
    for i in range(len(matrix2)):
        matrix.append(matrix2[i])
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print('------------------------------')
    print()


def result():
    probely()
    print('------------------------------')
    with open('result.txt', 'r') as data:
        res = json.load(data)
    matrix = []
    codes = []
    matrix2 = []
    for i in range(len(res)):
        ma = res[i][1].split()
        perem = ma[0] + ' ' + ma[1][0] + '.'
        if i == 0:
            matrix.append([perem, res[i][2], res[i][3], res[i][6], res[i][7], res[i][8]])
        else:
            if not (is_deleted(i)):
                if res[i][8] == 'Не посчитано':
                    matrix2.append([perem, res[i][2], res[i][3], res[i][6], res[i][7], res[i][8]])
                else:
                    matrix.append([perem, res[i][2], res[i][3], res[i][6], res[i][7], res[i][8]])
            else:
                codes.append(i)
    codes.sort()
    print('Рейтинговая таблица участников на данный момент')
    matrix1 = []
    for i in codes:
        ma = res[i][1].split()
        perem = ma[0] + ' ' + ma[1][0] + '.'
        matrix1.append([perem, res[i][2], res[i][3], res[i][6], res[i][7], res[i][8]])
    while True:
        c = 0
        for i in range(1, len(matrix) - 1):
            if matrix[i][5] < matrix[i + 1][5]:
                c = 1
                (matrix[i + 1], matrix[i]) = (matrix[i], matrix[i + 1])
        if c == 0:
            break
    for i in range(len(matrix1)):
        matrix.append(matrix1[i])
    for i in range(len(matrix2)):
        matrix.append(matrix2[i])
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print('------------------------------')
    print()


def emergency():
    probely()
    with open('result.txt', 'r') as data:
        res = json.load(data)
    codes = input('Введите код участника. Три цифры без лишних знаков: ')
    try:
        codes = int(codes)
        k = res[codes]
    except:
        print('Что-то пошло не так. Для сохранения данных выхожу из функции')
        return True
    for i in range(len(res[0])):
        print(res[0][i], res[codes][i], sep='')
    k = input('Напишите номер строки, которую хотите изменить. Это фиксируется! ENTER, если отмена')
    try:
        k = int(k) - 1
        i = res[codes][k]
    except:
        print('wrong data')
        return True
    print('Введите новое значение строки', res[codes][k], ': ')
    res[codes][k] = input()
    with open('result.txt', 'w') as data:
        json.dump(res, data)
    print('ok')


def commandsadmins():
    probely()
    print('Нажмите 1 для генерации новой работы')
    print('Нажмите 10 для удаления существующей работы')
    print('Нажмите 2 для внесения времени прохождения маршрута')
    print('Нажмите 3 для проверки работы')
    print('Нажмите 4 для просмотра таблицы участников')
    print('Нажмите 5 для выхода из вашей учётной записи')


def delete():
    probely()
    with open('deletedcodes.txt', 'r') as data:
        deleted_codes = json.load(data)
    with open('result.txt', 'r') as data:
        res = json.load(data)
    print('Восстановление удалённой ранее работы невозможно.')
    k = input('Вы собираетесь удалить работу. Подтвердите действие нажатием кнопки D: ')
    if k == 'd' or k == 'D' or k == 'В' or k == 'в':
        codes = input('Введите код работы, которую хотите удалить: ')
        try:
            codes = int(codes)
            k = res[codes]
        except:
            print('Что-то пошло не так. Для сохранения данных выхожу из функции')
            return True
        if is_deleted(codes):
            print('Работа удалена. Восстановление невозможно. Желаете изменить причину? Если да, введите DD:')
            l = input()
            if l == 'DD' or l == 'ВВ' or l == 'dd' or l == 'вв':
                deleted_codes.pop(is_deleted(-codes))
                print('Сейчас вы перейдёте к удалению работы, как будто она не удалена. Это не восстановление работы')
                delete()
                return True
        print('Вы удаляете работу участника', k[1], '. Подтвердите удалением вводом кода, иначе введите -1.')
        code1 = input('Введите код работы, которую хотите удалить: ')
        try:
            code1 = int(code1)
            if code1 != codes:
                print('Вводите тот же код. Попробуйте заново')
                return True
        except:
            print('Что-то пошло не так. Для сохранения данных выхожу из функции')
            return True
        print('Выберите причину удаления.')
        print('1: случайная генерация работы')
        print('2: неявка на старт')
        print('3: дисквалификация')
        print('Неверные данные можно поменять, обратитесь к сисадмину.')
        deleting_number = int(input('введите номер. Если желаете отменить удаление, вбейте -1. '))
        if deleting_number == 1:
            deleted_codes.append([res[codes][0], res[codes][1], res[codes][2], 'случ. генерация'])
            res[codes] = [res[codes][0], 'Тех. неполадки', 'OTP', '9999', [['-'], ['-'], ['-'], ['-'], ['-']], '0', '0',
                          '0', '0', '---']
        if deleting_number == 2:
            deleted_codes.append([res[codes][0], res[codes][1], res[codes][2], 'неявка'])
            res[codes] = [res[codes][0], res[codes][1], 'DNS', '9999', [['-'], ['-'], ['-'], ['-'], ['-']], '0', '0',
                          '0',
                          '0', '---']
        if deleting_number == 3:
            deleted_codes.append([res[codes][0], res[codes][1], res[codes][2], 'дисквалификация'])
            res[codes] = [res[codes][0], res[codes][1], 'DSQ', '9999', [['-'], ['-'], ['-'], ['-'], ['-']], '0', '0',
                          '0',
                          '0', '---']
        with open('deletedcodes.txt', 'w') as data:
            json.dump(deleted_codes, data)
        with open('result.txt', 'w') as data:
            json.dump(res, data)
        print('ok')


def easyencode(lol):
    probely()
    with open('result.txt', 'r') as data:
        res = json.load(data)
    with open('passwords.txt', 'r') as data:
        passwords = json.load(data)
    g = len(res)
    k = str(g)
    while len(k) < 3:
        k = '0' + k
    spis = ['Не внесено'] * 7
    spis.append('Не посчитано')
    spis.append('Не посчитано')
    spis.append('Не внесено')
    res.append(spis)
    res[-1][0] = k
    res[-1][1] = 'Тестовый' + k + ' Участник'
    res[-1][2] = '99T'
    ma = res[int(k)][1].split()
    perem = ma[1] + ma[0][0]
    with open('passwords.txt', 'r') as data:
        passwords = json.load(data)
    passwords.append([k, perem, 0])
    with open('passwords.txt', 'w') as data:
        json.dump(passwords, data)

    import random
    if lol:
        res[-1][3] = random.randint(150,450)
        res[-1][6] = random.randint(10,90)
        res[-1][7] = round(1 - (res[-1][3] - 300) / 180, 3)
        res[-1][8] = round(res[-1][6] * res[-1][7], 1)
        res[-1][9] = 'test'
    res[-1][4] = []
    global group_1
    global group_2
    global group_3
    global group_4
    global group_5
    random.shuffle(group_1)
    res[-1][4].append(group_1[0])
    random.shuffle(group_2)
    res[-1][4].append(group_2[0])
    random.shuffle(group_3)
    res[-1][4].append(group_3[0])
    random.shuffle(group_4)
    res[-1][4].append(group_4[0])
    random.shuffle(group_5)
    res[-1][4].append(group_5[0])
    random.shuffle(res[-1][4])
    bool = pdfgen(k, perem, res[int(k)][4])
    with open('result.txt', 'w') as data:
        json.dump(res, data)
    print('ok')


def otest():
    probely()
    print('сколько пустых работ?')
    k = int(input())
    for i in range(k):
        easyencode(False)
    print('сколько работ с внесением времени и баллов?')
    k = int(input())
    for i in range(k):
        easyencode(True)


def menu():
    print('MySistem----Menu')
    global login_now
    print('Введите логин Вашей учётной записи.')
    login = input()
    if login == '':
        print('Вы вошли в гостевую учётную запись')
        if members() == False:
            return True
    if login == '-':
        return True
    with open('passwords.txt', 'r') as data:
        mass = json.load(data)
    c = 0
    for i in range(len(mass)):
        if login in mass[i]:
            c = 1
            print('Введите пароль от этой учётки.')
            password = input()
            if password == mass[i][1]:
                print('Добро пожаловать!')
                login_now = login
                if mass[i][2] == 0:
                    if members() == False:
                        return True
                if mass[i][2] == 1:
                    if admin() == False:
                        return True
                if mass[i][2] == 2:
                    if sadmin() == False:
                        return True
            else:
                print('Пароль неверен. Попробуйте ещё раз')
                menu()
    if c == 0:
        print('Логин не найден. Попробуйте ещё раз.')
        menu()
    return True


def admin():
    while True:
        probely()
        print('Вы в главном меню. Для вызова функций меню введите 0.')
        type = input()
        try:
            if int(type) == 0:
                commandsadmins()
            elif int(type) == 1:
                encode()
            elif int(type) == 2:
                time()
            elif int(type) == 3:
                checkwork()
            elif int(type) == 4:
                resultadmins()
            elif int(type) == 10:
                delete()
            elif int(type) == 5:
                menu()
        except:
            print('try again')
            print()


def members():
    while True:
        probely()
        print('Вы в главном меню. Для вызова функций меню введите 0.')
        type = input()
        try:
            if int(type) == 0:
                commandsmembers()
            if int(type) == 1:
                result()
            if int(type) == 2:
                showmywork()
            if int(type) == 3:
                menu()
            elif int(type) == -999:
                return False
        except:
            print('try again')
            print()


def commandsmembers():
    probely()
    print('Введите 1 для просмотра рейтинговой таблицы участников')
    print('Введите 2 для просмотра информации о Вашей работе')
    print('Введите 3 для выхода из вашей учётной записи')


def commandssadmins():
    probely()
    print('Введите -1 для тестового ввода новых работ')
    print('Введите 1 для генерации новой работы')
    print('Введите 10 для удаления существующей работы')
    print('Введите 2 для внесения времени прохождения маршрута')
    print('Введите 3 для начала проверки работы')
    print('Введите 4 для просмотра таблицы участников')
    print('Введите 5 для выхода из вашей учётной записи')
    print('Введите 999 для изменения информации о работах')
    print('Введите 998 для очистки соревнования')
    print('Введите -999 для прерывания работы программы')


def clean():
    probely()
    print('Введите пароль от учётной записи')
    global login_now
    with open('result.txt', 'r') as data:
        res = json.load(data)
    with open('passwords.txt', 'r') as data:
        mass = json.load(data)
    for i in range(len(mass)):
        if login_now in mass[i]:
            password = input()
            if password in mass[i]:
                print('Доступ разрешён. Подтвердите очистку вводом кнопки D')
                k = input()
                if k == 'd' or k == 'D' or k == 'В' or k == 'в':
                    res = [['Код ', 'Фамилия Имя ', 'Класс ', 'Время (с) ',
                            [['Вопросы ', ], ['', ''], ['', ''], ['', ''], ['', '']], 'Баллы за вопросы ',
                            'Сумма баллов ', 'Коэф. за время ', 'Результат ', 'Проверено ', 'Скан']]
                    deleted_codes = [[000, 'Фамилия Имя', 'Класс', 'Причина удаления']]
                    passwords = [["matvej", "matvej", 2], ["samcs_admin", "samcs", 2], ["samcs_jury", "samcs", 1],["samcs_participant","samcs",0]]
                    with open('result.txt', 'w') as data:
                        json.dump(res, data)
                    with open('deletedcodes.txt', 'w') as data:
                        json.dump(deleted_codes, data)
                    with open('passwords.txt', 'w') as data:
                        json.dump(passwords, data)
                    # очистка листов участника
                    import os
                    import shutil

                    folder_path = "lists/"

                    if os.path.exists(folder_path):
                        shutil.rmtree(folder_path)  # Удаляет папку и всё внутри
                    print('Удаление завершено :)')


def sadmin():
    while True:
        probely()
        print()
        print('Вы в главном меню. Для вызова функций меню введите 0.')
        type = input()
        try:
            if int(type) == -1:
                otest()
            if int(type) == 0:
                commandssadmins()
            elif int(type) == 1:
                encode()
            elif int(type) == 2:
                time()
            elif int(type) == 3:
                checkwork()
            elif int(type) == 4:
                resultadmins()
            elif int(type) == 10:
                delete()
            elif int(type) == 999:
                emergency()
            elif int(type) == 5:
                menu()
            elif int(type) == 997:
                with open('result.txt', 'r') as data:
                    res = json.load(data)
                print(res)
            elif int(type) == 998:
                clean()
            elif int(type) == -999:
                return False
        except:
            print('try again')
            print()


def showmywork():
    probely()
    with open('result.txt', 'r') as data:
        res = json.load(data)
    codes = login_now
    try:
        codes = int(codes)
        k = res[codes]
        int(codes) != 0
    except:
        print('К Вашей учётной записи не прикреплено работы')
        return True
    for i in range(len(res[0])):
        if i != 4 and i != 5:
            print(res[0][i], res[codes][i], sep='')
        if i == 5:
            print(res[0][i], *res[codes][i])


def probely():
    print()
    print()
    print()
    print()


group_1 = [['A', 'Сторона света, на которую указывает азимут 90° '],
           ['B', 'Сторона света, на которую указывает азимут 180° '],
           ['C', 'Сторона света, на которую указывает азимут 270° '],
           ['D', 'Сторона света, на которую указывает азимут 360° '],
           ['E', 'Сторона света, на которую указывает азимут 0° ']]

group_2 = [['F', 'Самая высокая точка Северной Америки (название)'],
           ['G', 'Самая высокая точка Южной Америки (название)'], ['H', 'Самая высокая точка Африки (название)'],
           ['I', 'Самая высокая точка зарубежной Европы (название)'], ['J', 'Самая высокая точка Азии (название)']]

group_3 = [['K', 'Столица Уругвая'],
           ['L', 'Столица Колумбии'], ['M', 'Столица Венесуэлы'], ['N', 'Столица Перу'], ['O', 'Столица Чили']]

group_4 = [['P', 'Широта тропиков (°)'], ['Q', 'Широта полярных кругов (°)'],
           ['R', 'Длина экватора (приблизительно, км)'], ['S', 'Длина меридиана (приблизительно, км)'],
           ['T', 'Длина одного градуса меридиана (приблизительно, км)']]

group_5 = [['U','Определите вероятность того, что если проткнуть Землю насквозь, точки обеих проколов будут находиться на суше.'],
           ['V', 'Определите вероятность того, что если проткнуть Землю насквозь, точки обеих проколов будут находиться в воде.'],['W', 'Определите вероятность того, что если проткнуть Землю насквозь в точке, которая находится в воде, то точка второго прокола окажется на суше.'],['X',
            'Определите вероятность того, что если проткнуть Землю насквозь в точке, которая находится на суше, то точка второго прокола окажется в воде.'],['Y', 'В глобус, не глядя, ткнули булавку. На сколько отличаются вероятности попасть в воду и на сушу соответственно?']]


login_now = ''
menu()
