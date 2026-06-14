note = False
key = False
location_1_Description = False
location_2_Description = False
location_3_Description = False
location_position = 0

# приветствие и ввод имени игрока
print ("Добро пожалывать в игру Тайна заброшенной обсерватории")
player_name = input("Ведите имя игрока :")
print ("Добро пожаловать ", player_name, )

# игрока приветствует игра
input ("Нажмите Enter для продолжения")
print ("Сеттинг: Старая, заброшенная обсерватория на вершине холма, окутанная туманом. Главный герой", player_name, "ищет укрытие от внезапной бури.")
input ("Нажмите Enter чтобы перейти на Главный холл")


# Локация 1: Главный холл
def location_1():

    global location_1_Description, location_position
    location_position = 0

    print ("Главный холл")

    if location_1_Description == False:
        print ("Описание: Вы толкаете тяжелую дубовую дверь и оказываетесь в просторном холле. Пахнет старой бумагой и сыростью. Впереди — винтовая лестница, ведущая к главному телескопу. Справа — приоткрытая дверь в кабинет профессора. Назад выйти нельзя: буря заблокировала дверь снаружи.")
        location_1_Description = True
    
    print ("Выбор 1: Подняться по винтовой лестнице.")
    print ("Выбор 2: Зайти в кабинет профессора.")

    location_position = input ("Напиши 1 или 2 для выбора действия: ")

    if location_position == "1":
        location_2()
    elif location_position == "2":
        location_3()
    else:
        print ("Неверный выбор. Пожалуйста, выберите 1 или 2.")
        location_1()


# Локация 2: Главный телескоп
def location_2():

    global key, location_2_Description, location_position
    location_position = 0

    print("Главный телескоп")

    if location_2_Description == False:
        print ("Описание: Вы поднялись наверх. Здесь огромный старинный телескоп направлен в небо. На панели управления мигает красная лампочка — прибору нужно питание. На полу лежит странный медный ключ.")
        location_2_Description = True

    print ("Выбор 1: Взять ключ и вернуться в холл.")
    print ("Выбор 2: Попробовать включить телескоп без питания.")

    location_position = input ("Напиши 1 или 2 для выбора действия: ")

    if location_position == "1":
        key = True
        print ("Вы получили ключь")
        input ("Нажмите Enter что бы вернуться в Главный холл")
        location_1()
    elif location_position == "2":
        print ("Компьютер пишет: «Ничего не происходит»")
        input ("Нажмите Enter")
        location_2()
    else:
        print ("Неверный выбор. Пожалуйста, выберите 1 или 2.")
        location_2()

# Локация 3: Кабинет профессора
def location_3():

    global key, note, location_3_Description, location_position
    location_position = 0

    print ("Кабинет профессора")

    if location_3_Description == False:
        print ("Описание: В кабинете царит беспорядок. На столе стоит запертый сейф с замочной скважиной. В углу гудит старый генератор.")
        location_3_Description = True

    print ("Выбор 1: попробывать открыть сейф.")
    print ("Выбор 2: Включить генератор.")
    print ("Выбор 3: Вернуться в холл.")

    location_position = input ("Напиши 1, 2 или 3 для выбора действия: ")

    if location_position == "1":
        if key == False:
            print ("«Сейф заперт. Нужен ключ»")
            input ("Нажмите Enter")
            location_3()
        elif key == True:
            note = True
            print ("«Сейф открыт»")
            print ("Внутри лежит записка с кодом запуска генератора")
            input ("Нажмите Enter")
            location_3()

    elif location_position == "2":
        if note == False:
            print ("Вас убило током.")
            print ("Игра окончена.")
            before_release()
        elif note == True:
            print ("Вы запустили генератор.")
            print ("Обсерватория оживает, буря стихает!")
            print ("Победа.")
            before_release()

    elif location_position == "3":
        location_1()

    else:
        print ("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
        location_3()



# до выхода
def before_release():

    global note, key, end, location_1_Description, location_2_Description, location_3_Description, location_position

    print ("Чтобы выйти, введите 1, а чтобы начать снова, введите 2.")

    exit = input ()
    if exit == "2":
        note = False
        key = False
        location_1_Description = False
        location_2_Description = False
        location_3_Description = False
        location_position = 0
        location_1()

    elif exit == "1":
         exit

    else:
        print ("Неверный выбор. Пожалуйста, выберите 1 или 2.")
        before_release()

location_1()