note = False
key = False
location_1_Description = False
location_2_Description = False
location_3_Description = False
location_position = 0

# приветствие и ввод имени игрока
print ("========================================================")
print ("<Добро пожалывать в игру Тайна заброшенной обсерватории>")
print ("========================================================")
print ("")
player_name = input("Ведите своё игровое имя :")
print ("")
print ("")
print ("")
print ("Добро пожаловать ", player_name, )

# игрока приветствует игра
input ("<Нажмите> 'Enter' для продолжения")
print ("")
print ("")
print ("")
print ("<Сеттинг> Старая, заброшенная обсерватория на вершине холма, окутанная туманом. Главный герой", player_name, "ищет укрытие от внезапной бури.")
print ("")
input ("<Нажмите> 'Enter' чтобы перейти на ГЛАВНЫЙ ХОЛЛ")


# Локация 1: Главный холл
def location_1():

    global location_1_Description, location_position
    location_position = 0

    print ("")
    print ("")
    print ("")
    print ("ГЛАВНЫЙ ХОЛЛ")

    if location_1_Description == False:
        print ("")
        print ("<Описание> Вы толкаете тяжелую дубовую дверь и оказываетесь в просторном холле. Пахнет старой бумагой и сыростью. Впереди — винтовая лестница, ведущая к главному телескопу. Справа — приоткрытая дверь в кабинет профессора. Назад выйти нельзя: буря заблокировала дверь снаружи.")
        location_1_Description = True
    
    print ("")
    print ("<Выбор(2)> Подняться по винтовой лестнице.")
    print ("<Выбор(1)> Зайти в кабинет профессора.")

    print ("")
    location_position = input ("<Ведите 1 или 2 для выбора действия> : ")

    if location_position == "1":
        location_2()
    elif location_position == "2":
        location_3()
    else:
        print ("")
        print ("НЕВУРНЫЙ ВЫБОР! <Пожалуйста, выберите 1 или 2>")
        input ("<Нажмите> 'Enter' ")
        location_1()


# Локация 2: Главный телескоп
def location_2():

    global key, location_2_Description, location_position
    location_position = 0

    print ("")
    print ("")
    print ("")
    print("ГЛАВНЫЙ ТЕЛЕСКОП")

    if location_2_Description == False:
        print ("")
        print ("<Описание> Вы поднялись наверх. Здесь огромный старинный телескоп направлен в небо. На панели управления мигает красная лампочка — прибору нужно питание. На полу лежит странный медный ключ.")
        location_2_Description = True

    print ("")
    print ("<Выбор(1)> Взять ключ и вернуться в холл.")
    print ("<Выбор(2)> Попробовать включить телескоп без питания.")

    print ("")
    location_position = input ("<Ведите 1 или 2 для выбора действия> : ")

    if location_position == "1":
        if key == False:
            key = True
            print ("")
            print ("Вы получили ключь")
            input ("<Нажмите> 'Enter' что бы вернуться в ГЛАВНЫЙ ХОЛЛ")
            location_1()
        elif key == True:
            print ("")
            print ("Вы уже взяли ключь")
            input ("<Нажмите> 'Enter' что бы вернуться в ГЛАВНЫЙ ХОЛЛ")
    elif location_position == "2":
        print ("")
        print ("<Компьютер пишет> «ERROR....»")
        input ("<Нажмите> 'Enter'")
        location_2()
    else:
        print ("")
        print ("НЕВУРНЫЙ ВЫБОР! <Пожалуйста, выберите 1 или 2>")
        input ("<Нажмите> 'Enter'")
        location_2()

# Локация 3: Кабинет профессора
def location_3():

    global key, note, location_3_Description, location_position
    location_position = 0

    print ("")
    print ("")
    print ("")
    print ("КАБИНЕТ ПРОФЕССОРА")

    if location_3_Description == False:
        print ("")
        print ("<Описание> В кабинете царит беспорядок. На столе стоит запертый сейф с замочной скважиной. В углу гудит старый генератор.")
        location_3_Description = True

    print ("")
    print ("<Выбор(1)> попробывать открыть сейф.")
    print ("<Выбор(2)> Включить генератор.")
    print ("<Выбор(3)> Вернуться в холл.")

    print ("")
    location_position = input ("<Ведите 1, 2 или 3 для выбора действия> : ")

    if location_position == "1":
        if key == False:
            print ("")
            print ("«Сейф заперт. Нужен ключ»")
            input ("<Нажмите> 'Enter'")
            location_3()
        elif key == True:
            note = True
            print ("")
            print ("«Сейф открыт»")
            if note == False:
                print ("")
                print ("Внутри лежит записка с кодом запуска генератора")
                input ("<Нажмите> 'Enter'")
                location_3()
            elif note == True:
                print ("")
                print ("Внутри нечего нет")
                input ("<Нажмите> 'Enter'")
                location_3()
    elif location_position == "2":
        if note == False:
            print ("")
            print ("Вас убило током.")
            print ("Игра окончена.")
            input ("<Нажмите> 'Enter'")
            before_release()
        elif note == True:
            print ("")
            print ("Вы запустили генератор.")
            print ("Обсерватория оживает, буря стихает!")
            print ("Победа.")
            input ("<Нажмите> 'Enter'")
            before_release()

    elif location_position == "3":
        location_1()

    else:
        print ("")
        print ("НЕВУРНЫЙ ВЫБОР! <Пожалуйста, выберите 1, 2 или 3>")
        location_3()



# до выхода
def before_release():

    global note, key, location_1_Description, location_2_Description, location_3_Description, location_position

    print ("")
    print ("")
    print ("")
    print ("")
    print ("<Чтобы выйти, введите 1> <Чтобы начать снова, введите 2>")
    end = 0
    end = input ()
    if end == "2":
        note = False
        key = False
        location_1_Description = False
        location_2_Description = False
        location_3_Description = False
        location_position = 0
        location_1()

    elif end == "1":
         exit()

    else:
        print ("НЕВУРНЫЙ ВЫБОР! <Пожалуйста, выберите 1 или 2>")
        before_release()

location_1()