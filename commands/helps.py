
from vkbottle.bot import BotLabeler, Message
from config import help_text


bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text="помощь")
async def greeting(message: Message):
    return help_text


@bl.message(text=["время работы", "график", "часы работы", "1"])
async def greeting(message: Message):
    return "С 9:00 по 24:00"


@bl.message(text=["вход", '2'])
async def greeting(message: Message):
    text = '200Р с человека (пн-чт)\n' \
           '300Р с человека (пт-вс)\n' \
           'Дети до 8 лет со взрослыми бесплатно\n' \
           'Дети старше 8 лет:\n' \
           '100Р с человека (пн-чт)\n' \
           '150Р с человека (пт-вс)\n'
    return text

@bl.message(text=["стоянка", "парковка", '3'])
async def greeting(message: Message):
    text = 'День/ночь (12ч) 150 рублей\n' \
           'Сутки (24ч) 250 рублей\n'
    return text

@bl.message(text=["аренда беседки", "беседки", '4'])
async def greeting(message: Message):
    text = """
-Аренда открытой беседки до 24:00 2500 рублей, вход по прейскуранту.

-Аренда закрытой беседки с 9:00 до 24:00 5000 рублей, в стоимость входит посещение б-ти человек, следующие гости оплачивают посещение по прейскуранту.

    """
    return text


@bl.message(text=["аренда павильона", "павильон", '5'])
async def greeting(message: Message):
    text = """
Аренда павильона с 9:00 до 24:00 10000 рублей, посещение и стоянка автомобилей оплачивается отдельно по прейскуранту.

    """
    return text


@bl.message(text=["детские мероприятия", '6'])
async def greeting(message: Message):
    text = """
Детские мероприятия :
Дети до 8 лет 100 рублей с человека,
Дети старше 8 лет 150 рублей с человека

    """
    return text


@bl.message(text=["коттедж", '7'])
async def greeting(message: Message):
    text = """
Аренда коттеджа с хамамом 18000 рублей в сутки, 6 спальных мест.
Дополнительные гости оплачивают посещение по прейскуранту.
Стоянка 3-х машин.
Заезд в 14.00,выезд в 12.00.
Поздний выезд по согласованию, 1ч/1000 рублей, до 20.00/6000 рублей.
    """
    return text

@bl.message(text=["баня", '8', "аренда бани"])
async def greeting(message: Message):
    text = """
Аренда дом-бани 15000 рублей в сутки, 6 спальных мест
Дополнительные гости оплачивают посещение по прейскуранту.
Стоянка 3-х машин.
Березовый веник в подарок.
Заезд в 14.00,выезд в 12.00.
Поздний выезд по согласованию, 1ч/1000 рублей, до 20.00/6000 рублей.
Дополнительный березовый веник 250 рублей.

Аренда бани 1500 рублей час/минимум 4 часа, на 10 человек.
Березовый веник в подарок.
Дополнительные гости оплачивают 300рублей/человек.
Дополнительный березовый веник 250 рублей.
    """
    return text

@bl.message(text=["берег", '9'])
async def greeting(message: Message):
    text = """
Аренда шезлонга:
200 рублей с пн-чт
300 рублей с пт-вс

Аренда лодки
200 рублей с пн-чт
300 рублейс пт-вc

Аренда SUP-доски 400-00 рублей.

Аренда места для одной палатки 300-00 рублей в сутки, оплата за посещения по прейскуранту за каждый день проживания.

        """
    return text

@bl.message(text=["контакты", '10', "бронь"])
async def greeting(message: Message):
    text = '''
🌿Для бронирования и по всем вопросам обращаться👇🏻

☎ +7(922) 188-88-88

🌿https://bazauspeh.ru/

🌿При отказе от бронирования (менее 14 дней - при раннем и менее 48 часов -при обычном)
накладываются штрафные санкции - внесенная предоплата возврату не подлежит.
    
    '''
    return text


@bl.message(text=["правила", '11'])
async def greeting(message: Message):
    text = '''
ПРАВИЛА ПОВЕДЕНИЯ ОТДЫХАЮЩИХ НА ТЕРРИТОРИИ ЗАГОРОДНОГО КЛУБА «УСПЕХ»

На территории загородного клуба действуют правила и порядки, не противоречащие законодательным актам РФ.
Действие настоящих Правил распространяется на всех отдыхающих, находящихся на территории загородного клуба «Успех».


- Администрация и сотрудники загородного клуба "Успех" не несут ответственности за сохранность и целостность объектов материального имущества граждан (личные вещи, денежные средства и т.п.). 

- Вход на территорию загородного клуба с собаками ЗАПРЕЩЁН.

- Запрещается разжигать костры в неустановленных местах и на открытом грунте. 

- ЗАПРЕЩАЕТСЯ ШУМЕТЬ И ГРОМКО СЛУШАТЬ МУЗЫКУ ПОСЛЕ 23.00 ЧАСОВ.

- Запрещается нарушать отдых гостей, проживающих на территории загородного клуба, производить действия, нарушающие общественный порядок;

- Запрещается мусорить. Необходимо складывать мусор в бочки для мусора и контейнеры, которые повсеместно расположены на территории базы.

- Все отдыхающие обязаны бережно относиться к имуществу базы отдыха и окружающей среде.

- Запрещается употреблять наркотические и одурманивающие средства.

 ЖЕЛАЕМ ПРИЯТНОГО ОТДЫХА

    '''
    return text