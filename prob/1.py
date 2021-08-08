rus_cities = ['Абакан', 'Азов', 'Александров', 'Алексин', 'Альметьевск', 'Анапа', 'Ангарск', 'Анжеро-Судженск', 'Апатиты', 'Арзамас', 'Армавир', 'Арсеньев', 'Артем', 'Архангельск', 'Асбест', 'Астрахань', 'Ачинск', 'Балаково', 'Балахна', 'Балашиха', 'Балашов', 'Барнаул', 'Батайск', 'Белгород', 'Белебей', 'Белово', 'Белогорск', 'Белорецк', 'Белореченск', 'Бердск', 'Березники', 'Березовский', 'Бийск', 'Биробиджан', 'Благовещенск', 'Бор', 'Борисоглебск', 'Боровичи', 'Братск', 'Брянск', 'Бугульма', 'Буденновск', 'Бузулук', 'Буйнакск', 'Великие Луки', 'Великий Новгород', 'Верхняя Пышма', 'Видное', 'Владивосток', 'Владикавказ', 'Владимир', 'Волгоград', 'Волгодонск', 'Волжск', 'Волжский', 'Вологда', 'Вольск', 'Воркута', 'Воронеж', 'Воскресенск', 'Воткинск', 'Всеволожск', 'Выборг', 'Выкса', 'Вязьма', 'Гатчина', 'Геленджик', 'Георгиевск', 'Глазов', 'Горно-Алтайск', 'Грозный', 'Губкин', 'Гудермес', 'Гуково', 'Гусь-Хрустальный', 'Дербент', 'Дзержинск', 'Димитровград', 'Дмитров', 'Долгопрудный', 'Домодедово', 'Донской', 'Дубна', 'Евпатория', 'Егорьевск', 'Ейск', 'Екатеринбург', 'Елабуга', 'Елец', 'Ессентуки', 'Железногорск', 'Железногорск', 'Жигулевск', 'Жуковский', 'Заречный', 'Зеленогорск', 'Зеленодольск', 'Златоуст', 'Иваново', 'Ивантеевка', 'Ижевск', 'Избербаш', 'Иркутск', 'Искитим', 'Ишим', 'Ишимбай', 'Йошкар-Ола', 'Казань', 'Калининград', 'Калуга', 'Каменск-Уральский', 'Каменск-Шахтинский', 'Камышин', 'Канск', 'Каспийск', 'Кемерово', 'Керчь', 'Кинешма', 'Кириши', 'Киров', 'Кирово-Чепецк', 'Киселевск', 'Кисловодск', 'Клин', 'Клинцы', 'Ковров', 'Когалым', 'Коломна', 'Комсомольск-на-Амуре', 'Копейск', 'Королев', 'Кострома', 'Котлас', 'Красногорск', 'Краснодар', 'Краснокаменск', 'Краснокамск', 'Краснотурьинск', 'Красноярск', 'Кропоткин', 'Крымск', 'Кстово', 'Кузнецк', 'Кумертау', 'Кунгур', 'Курган', 'Курск', 'Кызыл', 'Лабинск', 'Лениногорск', 'Ленинск-Кузнецкий', 'Лесосибирск', 'Липецк', 'Лиски', 'Лобня', 'Лысьва', 'Лыткарино', 'Люберцы', 'Магадан', 'Магнитогорск', 'Майкоп', 'Махачкала', 'Междуреченск', 'Мелеуз', 'Миасс', 'Минеральные Воды', 'Минусинск', 'Михайловка', 'Михайловск', 'Мичуринск', 'Москва', 'Мурманск', 'Муром', 'Мытищи', 'Набережные Челны', 'Назарово', 'Назрань', 'Нальчик', 'Наро-Фоминск', 'Находка', 'Невинномысск', 'Нерюнгри', 'Нефтекамск', 'Нефтеюганск', 'Нижневартовск', 'Нижнекамск', 'Нижний Новгород', 'Нижний Тагил', 'Новоалтайск', 'Новокузнецк', 'Новокуйбышевск', 'Новомосковск', 'Новороссийск', 'Новосибирск', 'Новотроицк', 'Новоуральск', 'Новочебоксарск', 'Новочеркасск', 'Новошахтинск', 'Новый Уренгой', 'Ногинск', 'Норильск', 'Ноябрьск', 'Нягань', 'Обнинск', 'Одинцово', 'Озерск', 'Октябрьский', 'Омск', 'Орел', 'Оренбург', 'Орехово-Зуево', 'Орск', 'Павлово', 'Павловский Посад', 'Пенза', 'Первоуральск', 'Пермь', 'Петрозаводск', 'Петропавловск-Камчатский', 'Подольск', 'Полевской', 'Прокопьевск', 'Прохладный', 'Псков', 'Пушкино', 'Пятигорск', 'Раменское', 'Ревда', 'Реутов', 'Ржев', 'Рославль', 'Россошь', 'Ростов-на-Дону', 'Рубцовск', 'Рыбинск', 'Рязань', 'Салават', 'Сальск', 'Самара', 'Санкт-Петербург', 'Саранск', 'Сарапул', 'Саратов', 'Саров', 'Свободный', 'Севастополь', 'Северодвинск', 'Северск', 'Сергиев Посад', 'Серов', 'Серпухов', 'Сертолово', 'Сибай', 'Симферополь', 'Славянск-на-Кубани', 'Смоленск', 'Соликамск', 'Солнечногорск', 'Сосновый Бор', 'Сочи', 'Ставрополь', 'Старый Оскол', 'Стерлитамак', 'Ступино', 'Сургут', 'Сызрань', 'Сыктывкар', 'Таганрог', 'Тамбов', 'Тверь', 'Тимашевск', 'Тихвин', 'Тихорецк', 'Тобольск', 'Тольятти', 'Томск', 'Троицк', 'Туапсе', 'Туймазы', 'Тула', 'Тюмень', 'Узловая', 'Улан-Удэ', 'Ульяновск', 'Урус-Мартан', 'Усолье-Сибирское', 'Уссурийск', 'Усть-Илимск', 'Уфа', 'Ухта', 'Феодосия', 'Фрязино', 'Хабаровск', 'Ханты-Мансийск', 'Хасавюрт', 'Химки', 'Чайковский', 'Чапаевск', 'Чебоксары', 'Челябинск', 'Черемхово', 'Череповец', 'Черкесск', 'Черногорск', 'Чехов', 'Чистополь', 'Чита', 'Шадринск', 'Шали', 'Шахты', 'Шуя', 'Щекино', 'Щелково', 'Электросталь', 'Элиста', 'Энгельс', 'Южно-Сахалинск', 'Юрга', 'Якутск', 'Ялта', 'Ярославль']
from random import choice
town = choice(rus_cities)
print(town)
del rus_cities[rus_cities.index(town)]
temp = town[-1].upper()
temp_list = [i for i in rus_cities if i[0] == temp]
count = 2
if len(temp_list) == 0:
    temp = town[-count].upper()
print('Введите город на букву:', temp)
while True:
    print('Для выхода введите "стоп"')
    my_town = input()
    if my_town == 'стоп':
        print('Спасибо за игру, ждем Вас снова.')
        break
    if my_town not in rus_cities:
        print("Города не существует в России или он уже был назван")
        print('Введите город на букву:', temp)
    elif temp != my_town[0]:
        print('Введите город на букву:', temp)
    else:
        del rus_cities[rus_cities.index(my_town)]
        temp = my_town[-1].upper()
        temp_list = [i for i in rus_cities if i[0] == temp]
        if len(temp_list) > 0:
            town = choice(temp_list)
            temp = town[-1].upper()
            print(town)
            del rus_cities[rus_cities.index(town)]
            temp_list = [i for i in rus_cities if i[0] == temp]
            if len(temp_list) == 0:
                temp = town[-2].upper()
                print('Введите город на букву:', temp)
                count += 1
            else:
                print('Введите город на букву:', temp)
        else:
            temp_list = [i for i in rus_cities if i[0] == my_town[-2].upper()]
            town = choice(temp_list)
            temp = town[-1].upper()
            print(town)
            del rus_cities[rus_cities.index(town)]
            temp_list = [i for i in rus_cities if i[0] == temp]
            if len(temp_list) == 0:
                print('Введите город на букву:', temp)
                count += 1
            else:
                print('Введите город на букву:', temp)