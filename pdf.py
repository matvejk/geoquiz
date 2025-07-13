from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
# импорт кириллицы
pdfmetrics.registerFont(TTFont('Regular', 'Montserrat-Medium.ttf'))
pdfmetrics.registerFont(TTFont('Bold', 'Montserrat-Bold.ttf'))
code='009'
password='МатвейЕ'
tasks=[['X', 'Определите вероятность того, что если проткнуть Землю насквозь в точке, которая находится на суше, то точка второго прокола окажется в воде.'], ['O', 'Столица Чили'], ['B', 'Сторона света, на которую указывает азимут 180° '], ['G', 'Самая высокая точка Южной Америки (название)'], ['R', 'Длина экватора (приблизительно, км)']]
filename='Lists/'+code+'.pdf'
pdf_file = canvas.Canvas(filename, pagesize=A4)
width, height = A4 # x = 595 y = 841

# позиционирование для считывания
pdf_file.drawImage("granitsa.png", 50, height-390)
pdf_file.drawImage("granitsa.png", 534, height-390)
pdf_file.drawImage("granitsa.png", 50, height-670)
pdf_file.drawImage("granitsa.png", 534, height-670)

# хедэр
pdf_file.drawImage('logo.png',100,height-128-32,128,128)
pdf_file.setFont("Regular", 16)
pdf_file.drawString(250, height - 70-30, "География в школе 1502 | Гамма")
pdf_file.drawString(250, height - 90 -30, "Осенний географический квиз")
pdf_file.drawString(250, height - 110 -30, "ДД.ММ.ГГГГ")
pdf_file.setFont("Bold",18)
pdf_file.drawString(225, height - 180, "ЛИСТ УЧАСТНИКА")


pdf_file.setFont("Regular", 8)
pdf_file.drawString(50, height - 200, "0. Не используйте гаджеты и не списывайте у кого-либо. За это соревнование невозможно получить плохую оценку.")
pdf_file.drawString(50, height - 210, "1. В лист впечатаны буквы. За тридцать секунд до начала соревнования дежурный включит карту для")
pdf_file.drawString(50, height - 220, "определения позиций букв. Вы можете записывать месторасположения букв на свободном месте (НЕ в рамках!).")
pdf_file.drawString(50, height - 230, "2. Заносите ответы СТРОГО в предусмотренные рамки. Ответы за рамками проверяться и учитываться НЕ будут.")
pdf_file.drawString(50, height - 240, "Если Вам не хватило места, зачеркните ответ в основной рамке и пишите в дополнительной.")
pdf_file.drawString(50, height - 250, "При ответе в дополнительной рамке укажите букву вопроса рядом с ответом. Пишите строго внутри рамок.")
pdf_file.drawImage("primer.png", 100, height-305,400,50)
pdf_file.drawString(50, height - 310, "3. Учитывается время выполнения заданий. Самые быстрые 10% получат множитель π/e ≈ 1.16, медленные - e/π ≈ 0.87.")
pdf_file.drawString(50, height - 320, "При этом не разрешено бегать всегда, где это может быть опасно. Всегда нельзя бегать на лестницах.")
pdf_file.drawString(50, height - 330, "4. Нормативное время - 10 минут. Все результаты с временем, превышающим это, будут обнулены.")
pdf_file.drawString(50, height - 340, "5. Проходить по буквам не по порядку разрешается и приветствуется. Используйте время эффективно!")
pdf_file.setFont("Bold", 8)
pdf_file.drawString(50, height - 350, "Примите π ≈ 201/64. На Земле примерно 30% суши. Считайте, что суша распределена по Земле практически случайно.")
pdf_file.setFont("Bold", 16)
pdf_file.drawString(155, height - 380, f"Лист ответов. Код участника:        {code}")
pdf_file.rect(440, height-382, 50, 20, stroke=1, fill=0)

for i in range(len(tasks)):
    pdf_file.rect(50+30, height - 412 - 25*i, 50, 25, stroke=1, fill=0)
    pdf_file.drawString(65+30, height - 410 - 25*i, f"{tasks[i][0]}")
    pdf_file.rect(100+30, height - 412 - 25 * i, 400, 25, stroke=1, fill=0)

pdf_file.rect(50+30, height - 412 - 25 * 5 - 50 - 10, 450, 70, stroke=1, fill=0)

pdf_file.setFont("Regular", 12)
pdf_file.drawString(50, height - 412 - 25 * 5 - 50 - 10-15-10, "Организатор, занеси время выполнения в поле справа:")
pdf_file.rect(430, height - 412 - 25 * 5 - 50 - 10-15-12-10, 100, 30, stroke=1, fill=0)
pdf_file.setFont("Regular", 8)
pdf_file.drawString(50, height - 690, f"Эта часть листа остаётся у участника. После проверки вы сможете")
pdf_file.drawString(50, height - 700, f"просмотреть свой результат в telegram-боте.")
pdf_file.drawString(50, height - 710, f"При первом входе в бот введите свой логин: {code}, пароль - {password}.")
pdf_file.drawString(50, height - 720, f"Для захода в бот перейдите по QR-коду слева или введите")
pdf_file.drawString(50, height - 730, f"прямую ссылку: t.me/Quiz1502Bot")


pdf_file.drawImage('tglink.png',350,height-820,150,150)

pdf_file.showPage()
pdf_file.save()
