import keyboard
import random #Looxi lox
from colorama import Fore  #Looxi lox
def Revolution():
    Gloves = [
              "★ Спортивные перчатки | Порок",
              "★ Перчатки спецназа | Градиент",
              "★ Спортивные перчатки | Амфибия",
              "★ Спортивные перчатки | Омега",
              "★ Мотоциклетные перчатки | БУХ!",
              "★ Перчатки спецназа | Кровавая паутина",
              "★ Водительские перчатки | Королевский змей",
              "★ Обмотки рук | Синие черепа",
              "★ Мотоциклетные перчатки | Черепаха",
              "★ Перчатки спецназа | Покоритель гор",
              "★ Обмотки рук | Оттиск",
              "★ Водительские перчатки | Обгон",
              "★ Водительские перчатки | Имперская клетка",
              "★ Мотоциклетные перчатки | Транспорт",
              "★ Перчатки спецназа | Дробь",
              "★ Перчатки «Гидра» | Поверхностная закалка",
              "★ Водительские перчатки | Гоночный зелёный",
              "★ Мотоциклетные перчатки | Полигон",
              "★ Спортивные перчатки | Окисление бронзы",
              "★ Обмотки рук | Лес",
              "★ Перчатки «Гидра» | Изумруд",
              "★ Обмотки рук | Скотч",
              "★ Перчатки «Гидра» | Гремучая змея",
              "★ Перчатки «Гидра» | Мангры"]
    x1 = ["AK-47 | Head Shot",
          "M4A4 | Temukau"]
    y1 = ["AWP | Duality",
          "P2000 | Wicked Sick",
          "UMP-45 | Wild Child"]
    a1 = ["M4A1-S | Emphorosaur-S",
          "Glock-18 | Umbral Rabbit",
          "MAC-10 | Sakkaku",
          "R8 Revolver | Banana Cannon",
          "P90 | Neoqueen"]
    b1 = ["MAG-7 | Insomnia",
          "MP9 | Featherweight",
          "SCAR-20 | Fragments",
          "P250 | Re.built",
          "MP5-SD | Liquidation",
          "SG 553 | Cyberforce",
          "Tec-9 | Rebel"]
    global b, a, y, x
    b = 0
    a = 0
    y = 0
    x = 0
    g = 0
    b = (random.randrange(1, 9))
    a = (random.randrange(1, 7))
    y = (random.randrange(1, 5))
    x = (random.randrange(1, 4))
    if b == 1 or b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7:
        b = (random.randrange(0, 7))
        print(Fore.BLUE + b1[b])
    elif a == 1 or a == 2 or a == 3 or a == 4 or a == 5:
        a = (random.randrange(0, 5))
        print(Fore.MAGENTA + a1[a])
    elif y == 1 or y == 2 or y == 3:
        y = (random.randrange(0, 2))
        print(Fore.LIGHTMAGENTA_EX + y1[y])
    elif x == 1 or x == 2:
        x = (random.randrange(0, 2))
        print(Fore.LIGHTRED_EX + x1[x])
    elif g == 0:
        g = (random.randrange(0, 24))
        print(Fore.LIGHTYELLOW_EX + Gloves[g])
def Recoil():
    Gloves = [
              "★ Перчатки спецназа | Удар тигра",
              "★ Перчатки спецназа | Мраморный градиент",
              "★ Спортивные перчатки | Мясник",
              "★ Водительские перчатки | Черный галстук",
              "★ Мотоциклетные перчатки | Кровяное давление",
              "★ Водительские перчатки | Снежный барс",
              "★ Перчатки спецназа | Полевой агент",
              "★ Спортивные перчатки | Ноктс",
              "★ Спортивные перчатки | Кровавый шемах",
              "★ Спортивные перчатки | Крупная добыча",
              "★ Мотоциклетные перчатки | Третья рота коммандо",
              "★ Мотоциклетные перчатки | Бросаю дымовую",
              "★ Обмотки рук | ОСТОРОЖНО!",
              "★ Мотоциклетные перчатки | Финишная линия",
              "★ Перчатки спецназа | Капитан 3-го ранга",
              "★ Перчатки «Сломанный клык» | Без тормозов",
              "★ Перчатки «Сломанный клык» | Нефрит",
              "★ Перчатки «Сломанный клык» | Остриё иглы",
              "★ Водительские перчатки | Резан Красный",
              "★ Водительские перчатки | Королева ягуаров",
              "★ Обмотки рук | Жираф",
              "★ Перчатки «Сломанный клык» | Жёлтые полосы",
              "★ Обмотки рук | Удав",
              "★ Обмотки рук | Пустынный шемах"]
    x1 = ["USP-S | Printstream",
          "AWP | Chromatic Aberration"]
    y1 = ["AK-47 | Ice Coaled",
          "P250 | Visions",
          "Sawed-Off | Kiss♥Love"]
    a1 = ["R8 Revolver | Crazy 8",
          "M249 | Downtown",
          "SG 553 | Dragon Tech",
          "P90 | Vent Rush",
          "Dual Berettas | Flora Carnivora"]
    b1 = ["FAMAS | Meow 36",
          "Galil AR | Destroyer",
          "M4A4 | Poly Mag",
          "MAC-10 | Monkeyflage",
          "Negev | Drop Me",
          "UMP-45 | Roadblock",
          "Glock-18 | Winterized"]
    global b, a, y, x
    b = 0
    a = 0
    y = 0
    x = 0
    g = 0
    b = (random.randrange(1, 9))
    a = (random.randrange(1, 7))
    y = (random.randrange(1, 5))
    x = (random.randrange(1, 4))
    if b == 1 or b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7:
        b = (random.randrange(0, 7))
        print(Fore.BLUE + b1[b])
    elif a == 1 or a == 2 or a == 3 or a == 4 or a == 5:
        a = (random.randrange(0, 5))
        print(Fore.MAGENTA + a1[a])
    elif y == 1 or y == 2 or y == 3:
        y = (random.randrange(0, 2))
        print(Fore.LIGHTMAGENTA_EX + y1[y])
    elif x == 1 or x == 2:
        x = (random.randrange(0, 2))
        print(Fore.LIGHTRED_EX + x1[x])
    elif g == 0:
        g = (random.randrange(0, 24))
        print(Fore.LIGHTYELLOW_EX + Gloves[g])
def Nightmares():
    Knife = [
             "★ Butterfly Knife | Gamma Doppler Emerald",
             "★ Butterfly Knife | Lore",
             "★ Huntsman Knife | Gamma Doppler Emerald",
             "★ Butterfly Knife | Gamma Doppler Phase 4",
             "★ Butterfly Knife | Autotronic",
             "★ Butterfly Knife | Gamma Doppler Phase 2",
             "★ Bowie Knife | Gamma Doppler Emerald",
             "★ Butterfly Knife | Gamma Doppler Phase 3",
             "★ Butterfly Knife | Gamma Doppler Phase 1",
             "★ Falchion Knife | Gamma Doppler Emerald",
             "★ Butterfly Knife | Black Laminate",
             "★ Shadow Daggers | Gamma Doppler Emerald",
             "★ Butterfly Knife | Freehand",
             "★ Butterfly Knife | Bright Water",
             "★ Bowie Knife | Lore",
             "★ Huntsman Knife | Gamma Doppler Phase 2",
             "★ Huntsman Knife | Gamma Doppler Phase 4",
             "★ Huntsman Knife | Lore",
             "★ Huntsman Knife | Gamma Doppler Phase 1",
             "★ Bowie Knife | Gamma Doppler Phase 4",
             "★ Shadow Daggers | Lore",
             "★ Huntsman Knife | Gamma Doppler Phase 3",
             "★ Huntsman Knife | Autotronic",
             "★ Falchion Knife | Gamma Doppler Phase 4",
             "★ Bowie Knife | Gamma Doppler Phase 1",
             "★ Bowie Knife | Gamma Doppler Phase 2",
             "★ Bowie Knife | Gamma Doppler Phase 3",
             "★ Falchion Knife | Gamma Doppler Phase 2",
             "★ Falchion Knife | Gamma Doppler Phase 1",
             "★ Falchion Knife | Autotronic",
             "★ Bowie Knife | Autotronic",
             "★ Falchion Knife | Lore",
             "★ Falchion Knife | Gamma Doppler Phase 3",
             "★ Shadow Daggers | Gamma Doppler Phase 4",
             "★ Huntsman Knife | Black Laminate",
             "★ Bowie Knife | Black Laminate",
             "★ Shadow Daggers | Gamma Doppler Phase 2",
             "★ Shadow Daggers | Gamma Doppler Phase 3",
             "★ Shadow Daggers | Gamma Doppler Phase 1",
             "★ Shadow Daggers | Autotronic",
             "★ Huntsman Knife | Freehand",
             "★ Falchion Knife | Black Laminate",
             "★ Bowie Knife | Freehand",
             "★ Falchion Knife | Freehand",
             "★ Huntsman Knife | Bright Water",
             "★ Bowie Knife | Bright Water",
             "★ Shadow Daggers | Black Laminate",
             "★ Falchion Knife | Bright Water",
             "★ Shadow Daggers | Freehand",
             "★ Shadow Daggers | Bright Water"]
    x1 = ["AK-47 | Nightwish",
          "MP9 | Starlight Protector"]
    y1 = ["Dual Berettas | Melondrama",
          "FAMAS | Rapid Eye Movement",
          "MP7 | Abyssal Apparition"]
    a1 = ["PP-Bizon | Space Cat",
          "G3SG1 | Dream Glade",
          "M4A1-S | Night Terror",
          "XM1014 | Zombie Offensive",
          "USP-S | Ticket to Hell"]
    b1 = ["Five-SeveN | Scrawl",
          "MAC-10 | Ensnared",
          "MAG-7 | Foresight",
          "MP5-SD | Necro Jr.",
          "P2000 | Lifted Spirits",
          "SCAR-20 | Poultrygeist",
          "Sawed-Off | Spirit Board"]
    global b, a, y, x, k
    b = 0
    a = 0
    y = 0
    x = 0
    k = 0
    b = (random.randrange(1, 9))
    a = (random.randrange(1, 7))
    y = (random.randrange(1, 5))
    x = (random.randrange(1, 4))
    if b == 1 or b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7:
        b = (random.randrange(0, 7))
        print(Fore.BLUE + b1[b])
    elif a == 1 or a == 2 or a == 3 or a == 4 or a == 5:
        a = (random.randrange(0, 5))
        print(Fore.MAGENTA + a1[a])
    elif y == 1 or y == 2 or y == 3:
        y = (random.randrange(0, 3))
        print(Fore.LIGHTMAGENTA_EX + y1[y])
    elif x == 1 or x == 2:
        x = (random.randrange(0, 2))
        print(Fore.LIGHTRED_EX + x1[x])
    elif k == 0:
        k = (random.randrange(0, 49))
        print(Fore.LIGHTYELLOW_EX + Knife[k])
def Riptide():
    Knife = [
             "★ Butterfly Knife | Gamma Doppler Emerald",
             "★ Butterfly Knife | Lore",
             "★ Huntsman Knife | Gamma Doppler Emerald",
             "★ Butterfly Knife | Gamma Doppler Phase 4",
             "★ Butterfly Knife | Autotronic",
             "★ Butterfly Knife | Gamma Doppler Phase 2",
             "★ Bowie Knife | Gamma Doppler Emerald",
             "★ Butterfly Knife | Gamma Doppler Phase 3",
             "★ Butterfly Knife | Gamma Doppler Phase 1",
             "★ Falchion Knife | Gamma Doppler Emerald",
             "★ Butterfly Knife | Black Laminate",
             "★ Shadow Daggers | Gamma Doppler Emerald",
             "★ Butterfly Knife | Freehand",
             "★ Butterfly Knife | Bright Water",
             "★ Bowie Knife | Lore",
             "★ Huntsman Knife | Gamma Doppler Phase 2",
             "★ Huntsman Knife | Gamma Doppler Phase 4",
             "★ Huntsman Knife | Lore",
             "★ Huntsman Knife | Gamma Doppler Phase 1",
             "★ Bowie Knife | Gamma Doppler Phase 4",
             "★ Shadow Daggers | Lore",
             "★ Huntsman Knife | Gamma Doppler Phase 3",
             "★ Huntsman Knife | Autotronic",
             "★ Falchion Knife | Gamma Doppler Phase 4",
             "★ Bowie Knife | Gamma Doppler Phase 1",
             "★ Bowie Knife | Gamma Doppler Phase 2",
             "★ Bowie Knife | Gamma Doppler Phase 3",
             "★ Falchion Knife | Gamma Doppler Phase 2",
             "★ Falchion Knife | Gamma Doppler Phase 1",
             "★ Falchion Knife | Autotronic",
             "★ Bowie Knife | Autotronic",
             "★ Falchion Knife | Lore",
             "★ Falchion Knife | Gamma Doppler Phase 3",
             "★ Shadow Daggers | Gamma Doppler Phase 4",
             "★ Huntsman Knife | Black Laminate",
             "★ Bowie Knife | Black Laminate",
             "★ Shadow Daggers | Gamma Doppler Phase 2",
             "★ Shadow Daggers | Gamma Doppler Phase 3",
             "★ Shadow Daggers | Gamma Doppler Phase 1",
             "★ Shadow Daggers | Autotronic",
             "★ Huntsman Knife | Freehand",
             "★ Falchion Knife | Black Laminate",
             "★ Bowie Knife | Freehand",
             "★ Falchion Knife | Freehand",
             "★ Huntsman Knife | Bright Water",
             "★ Bowie Knife | Bright Water",
             "★ Shadow Daggers | Black Laminate",
             "★ Falchion Knife | Bright Water",
             "★ Shadow Daggers | Freehand",
             "★ Shadow Daggers | Bright Water",]
    x1 = ["Desert Eagle | Ocean Drive",
          "AK-47 | Leet Museo"]
    y1 = ["MAC-10 | Toybox",
          "Glock-18 | Snack Attack",
          "SSG 08 | Turbo Peek"]
    a1 = ["MAG-7 | BI83 Spectrum",
          "FAMAS | ZX Spectron",
          "Five-SeveN | Boost Protocol",
          "MP9 | Mount Fuji",
          "M4A4 | Spider Lily"]
    b1 = ["AUG | Plague",
          "Dual Berettas | Tread",
          "G3SG1 | Keeping Tabs",
          "MP7 | Guerrilla",
          "PP-Bizon | Lumen",
          "USP-S | Black Lotus",
          "XM1014 | Watchdog"]
    global b, a, y, x
    b = 0
    a = 0
    y = 0
    x = 0
    k = 0
    b = (random.randrange(1, 9))
    a = (random.randrange(1, 7))
    y = (random.randrange(1, 5))
    x = (random.randrange(1, 4))
    if b == 1 or b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7:
        b = (random.randrange(0, 7))
        print(Fore.BLUE + b1[b])
    elif a == 1 or a == 2 or a == 3 or a == 4 or a == 5:
        a = (random.randrange(0, 5))
        print(Fore.MAGENTA + a1[a])
    elif y == 1 or y == 2 or y == 3:
        y = (random.randrange(0, 2))
        print(Fore.LIGHTMAGENTA_EX + y1[y])
    elif x == 1 or x == 2:
        x = (random.randrange(0, 2))
        print(Fore.LIGHTRED_EX + x1[x])
    elif k == 0:
        k = (random.randrange(0, 24))
        print(Fore.LIGHTYELLOW_EX + Knife[k])
def Fracture():
    Knife = [
             "★ Skeleton Knife | Fade",
             "★ Skeleton Knife | Crimson Web",
             "★ Skeleton Knife | Case Hardened",
             "★ Nomad Knife | Fade",
             "★ Skeleton Knife | Slaughter",
             "★ Skeleton Knife | Vanilla",
             "★ Skeleton Knife | Blue Steel",
             "★ Nomad Knife | Crimson Web",
             "★ Skeleton Knife | Stained",
             "★ Paracord Knife | Fade",
             "★ Survival Knife | Fade",
             "★ Nomad Knife | Slaughter",
             "★ Nomad Knife | Vanilla",
             "★ Skeleton Knife | Urban Masked",
             "★ Nomad Knife | Case Hardened",
             "★ Skeleton Knife | Night Stripe",
             "★ Nomad Knife | Blue Steel",
             "★ Nomad Knife | Stained",
             "★ Paracord Knife | Crimson Web",
             "★ Paracord Knife | Slaughter",
             "★ Paracord Knife | Case Hardened",
             "★ Survival Knife | Crimson Web",
             "★ Survival Knife | Slaughter",
             "★ Paracord Knife | Vanilla",
             "★ Survival Knife | Vanilla",
             "★ Skeleton Knife | Forest DDPAT",
             "★ Skeleton Knife | Boreal Forest",
             "★ Nomad Knife | Boreal Forest",
             "★ Skeleton Knife | Safari Mesh",
             "★ Skeleton Knife | Scorched",
             "★ Survival Knife | Night Stripe",
             "★ Paracord Knife | Stained",
             "★ Paracord Knife | Blue Steel",
             "★ Paracord Knife | Boreal Forest",
             "★ Paracord Knife | Night Stripe",
             "★ Survival Knife | Stained",
             "★ Nomad Knife | Night Stripe",
             "★ Survival Knife | Blue Steel",
             "★ Nomad Knife | Urban Masked",
             "★ Survival Knife | Case Hardened",
             "★ Survival Knife | Urban Masked",
             "★ Nomad Knife | Forest DDPAT",
             "★ Survival Knife | Forest DDPAT",
             "★ Nomad Knife | Scorched",
             "★ Nomad Knife | Safari Mesh",
             "★ Survival Knife | Boreal Forest",
             "★ Paracord Knife | Scorched",
             "★ Paracord Knife | Urban Masked",
             "★ Paracord Knife | Forest DDPAT",
             "★ Paracord Knife | Safari Mesh",
             "★ Survival Knife | Scorched",
             "★ Survival Knife | Safari Mesh",]
    x1 = ["Desert Eagle | Printstream",
          "AK-47 | Legion of Anubis"]
    y1 = ["M4A4 | Tooth Fairy",
          "Glock-18 | Vogue",
          "XM1014 | Entombed"]
    a1 = ["MAG-7 | Monster Call",
          "Tec-9 | Brother",
          "MAC-10 | Allure",
          "Galil AR | Connexion",
          "MP5-SD | Kitbash"]
    b1 = ["Negev | Ultralight",
          "P2000 | Gnarled",
          "SG 553 | Ol' Rusty",
          "SSG 08 | Mainframe 001",
          "P250 | Cassette",
          "P90 | Freight",
          "PP-Bizon | Runic"]

    global b, a, y, x
    b = 0
    a = 0
    y = 0
    x = 0
    k = 0
    b = (random.randrange(1, 9))
    a = (random.randrange(1, 7))
    y = (random.randrange(1, 5))
    x = (random.randrange(1, 4))
    if b == 1 or b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7:
        b = (random.randrange(0, 7))
        print(Fore.BLUE + b1[b])
    elif a == 1 or a == 2 or a == 3 or a == 4 or a == 5:
        a = (random.randrange(0, 5))
        print(Fore.MAGENTA + a1[a])
    elif y == 1 or y == 2 or y == 3:
        y = (random.randrange(0, 2))
        print(Fore.LIGHTMAGENTA_EX + y1[y])
    elif x == 1 or x == 2:
        x = (random.randrange(0, 2))
        print(Fore.LIGHTRED_EX + x1[x])
    elif k == 0:
        k = (random.randrange(0, 51))
        print(Fore.LIGHTYELLOW_EX + Knife[k])
def Gamma2():
    Knife = [
             "★ M9 Bayonet | Gamma Doppler Emerald",
             "★ Karambit | Gamma Doppler Emerald",
             "★ Bayonet | Gamma Doppler Emerald",
             "★ Flip Knife | Gamma Doppler Emerald",
             "★ M9 Bayonet | Lore",
             "★ Karambit | Lore",
             "★ Karambit | Gamma Doppler Phase 2",
             "★ Karambit | Autotronic",
             "★ M9 Bayonet | Gamma Doppler Phase 2",
             "★ M9 Bayonet | Autotronic",
             "★ M9 Bayonet | Gamma Doppler Phase 4",
             "★ Karambit | Gamma Doppler Phase 4",
             "★ Karambit | Gamma Doppler Phase 3",
             "★ Karambit | Black Laminate",
             "★ M9 Bayonet | Gamma Doppler Phase 3",
             "★ Karambit | Gamma Doppler Phase 1",
             "★ Gut Knife | Gamma Doppler Emerald",
             "★ M9 Bayonet | Gamma Doppler Phase 1",
             "★ Bayonet | Lore",
             "★ Bayonet | Gamma Doppler Phase 2",
             "★ M9 Bayonet | Black Laminate",
             "★ Bayonet | Autotronic",
             "★ Bayonet | Gamma Doppler Phase 4",
             "★ Flip Knife | Gamma Doppler Phase 2",
             "★ Karambit | Freehand",
             "★ Bayonet | Gamma Doppler Phase 3"
             "★ Bayonet | Gamma Doppler Phase 1",
             "★ Karambit | Bright Water",
             "★ Flip Knife | Lore",
             "★ Flip Knife | Autotronic",
             "★ Flip Knife | Gamma Doppler Phase 3",
             "★ M9 Bayonet | Freehand",
             "★ M9 Bayonet | Bright Water",
             "★ Bayonet | Black Laminate",
             "★ Flip Knife | Gamma Doppler Phase 4",
             "★ Flip Knife | Doppler Phase 2",
             "★ Flip Knife | Doppler Phase 4",
             "★ Flip Knife | Gamma Doppler Phase 1",
             "★ Flip Knife | Doppler Phase 1",
             "★ Flip Knife | Doppler Phase 3",
             "★ Flip Knife | Black Laminate",
             "★ Bayonet | Freehand",
             "★ Bayonet | Bright Water",
             "★ Gut Knife | Autotronic",
             "★ Gut Knife | Lore",
             "★ Flip Knife | Freehand",
             "★ Gut Knife | Gamma Doppler Phase 2",
             "★ Flip Knife | Bright Water",
             "★ Gut Knife | Gamma Doppler Phase 4",
             "★ Gut Knife | Gamma Doppler Phase 3",
             "★ Gut Knife | Gamma Doppler Phase 1",
             "★ Gut Knife | Doppler Phase 2",
             "★ Gut Knife | Black Laminate",
             "★ Gut Knife | Doppler Phase 3",
             "★ Gut Knife | Freehand",
             "★ Gut Knife | Bright Water"]
    x1 = ["AK-47 | Neon Revolution",
          "FAMAS | Roll Cage"]
    y1 = ["AUG | Syd Mead",
          "MP9 | Airlock",
          "Tec-9 | Fuel Injector"]
    a1 = ["Desert Eagle | Directive",
          "Glock-18 | Weasel",
          "MAG-7 | Petroglyph",
          "SCAR-20 | Powercore",
          "SG 553 | Triarch"]
    b1 = ["CZ75-Auto | Imprint",
          "Five-SeveN | Scumbria",
          "G3SG1 | Ventilator",
          "Negev | Dazzle",
          "P90 | Grim",
          "UMP-45 | Briefing",
          "XM1014 | Slipstream"]
    global b, a, y, x
    b = 0
    a = 0
    y = 0
    x = 0
    k = 0
    b = (random.randrange(1, 9))
    a = (random.randrange(1, 7))
    y = (random.randrange(1, 5))
    x = (random.randrange(1, 4))
    if b == 1 or b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7:
        b = (random.randrange(0, 7))
        print(Fore.BLUE + b1[b])
    elif a == 1 or a == 2 or a == 3 or a == 4 or a == 5:
        a = (random.randrange(0, 5))
        print(Fore.MAGENTA + a1[a])
    elif y == 1 or y == 2 or y == 3:
        y = (random.randrange(0, 2))
        print(Fore.LIGHTMAGENTA_EX + y1[y])
    elif x == 1 or x == 2:
        x = (random.randrange(0, 2))
        print(Fore.LIGHTRED_EX + x1[x])
    elif k == 0:
        k = (random.randrange(0, 24))
        print(Fore.LIGHTYELLOW_EX + Knife[k])
def Gamma():
    Knife = [
             "★ M9 Bayonet | Gamma Doppler Emerald",
             "★ Karambit | Gamma Doppler Emerald",
             "★ Bayonet | Gamma Doppler Emerald",
             "★ Flip Knife | Gamma Doppler Emerald",
             "★ M9 Bayonet | Lore",
             "★ Karambit | Lore",
             "★ Karambit | Gamma Doppler Phase 2",
             "★ Karambit | Autotronic",
             "★ M9 Bayonet | Gamma Doppler Phase 2",
             "★ M9 Bayonet | Autotronic",
             "★ M9 Bayonet | Gamma Doppler Phase 4",
             "★ Karambit | Gamma Doppler Phase 4",
             "★ Karambit | Gamma Doppler Phase 3",
             "★ Karambit | Black Laminate",
             "★ M9 Bayonet | Gamma Doppler Phase 3",
             "★ Karambit | Gamma Doppler Phase 1",
             "★ Gut Knife | Gamma Doppler Emerald",
             "★ M9 Bayonet | Gamma Doppler Phase 1",
             "★ Bayonet | Lore",
             "★ Bayonet | Gamma Doppler Phase 2",
             "★ M9 Bayonet | Black Laminate",
             "★ Bayonet | Autotronic",
             "★ Bayonet | Gamma Doppler Phase 4",
             "★ Flip Knife | Gamma Doppler Phase 2",
             "★ Karambit | Freehand",
             "★ Bayonet | Gamma Doppler Phase 3"
             "★ Bayonet | Gamma Doppler Phase 1",
             "★ Karambit | Bright Water",
             "★ Flip Knife | Lore",
             "★ Flip Knife | Autotronic",
             "★ Flip Knife | Gamma Doppler Phase 3",
             "★ M9 Bayonet | Freehand",
             "★ M9 Bayonet | Bright Water",
             "★ Bayonet | Black Laminate",
             "★ Flip Knife | Gamma Doppler Phase 4",
             "★ Flip Knife | Doppler Phase 2",
             "★ Flip Knife | Doppler Phase 4",
             "★ Flip Knife | Gamma Doppler Phase 1",
             "★ Flip Knife | Doppler Phase 1",
             "★ Flip Knife | Doppler Phase 3",
             "★ Flip Knife | Black Laminate",
             "★ Bayonet | Freehand",
             "★ Bayonet | Bright Water",
             "★ Gut Knife | Autotronic",
             "★ Gut Knife | Lore",
             "★ Flip Knife | Freehand",
             "★ Gut Knife | Gamma Doppler Phase 2",
             "★ Flip Knife | Bright Water",
             "★ Gut Knife | Gamma Doppler Phase 4",
             "★ Gut Knife | Gamma Doppler Phase 3",
             "★ Gut Knife | Gamma Doppler Phase 1",
             "★ Gut Knife | Doppler Phase 2",
             "★ Gut Knife | Black Laminate",
             "★ Gut Knife | Doppler Phase 3",
             "★ Gut Knife | Freehand",
             "★ Gut Knife | Bright Water"]
    x1 = ["Glock-18 | Wasteland Rebel",
          "M4A1-S | Mecha Industries"]
    y1 = ["M4A4 | Desolate Space",
          "P2000 | Imperial Dragon",
          "SCAR-20 | Bloodsport"]
    a1 = ["AUG | Aristocrat",
          "AWP | Phobos",
          "P90 | Chopper",
          "R8 Revolver | Reboot",
          "Sawed-Off | Limelight"]
    b1 = ["Five-SeveN | Violent Daimyo",
          "MAC-10 | Carnivore",
          "Nova | Exo",
          "P250 | Iron Clad",
          "PP-Bizon | Harvester",
          "SG 553 | Aerial",
          "Tec-9 | Ice Cap"]
    global b, a, y, x
    b = 0
    a = 0
    y = 0
    x = 0
    k = 0
    b = (random.randrange(1, 9))
    a = (random.randrange(1, 7))
    y = (random.randrange(1, 5))
    x = (random.randrange(1, 4))
    if b == 1 or b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7:
        b = (random.randrange(0, 7))
        print(Fore.BLUE + b1[b])
    elif a == 1 or a == 2 or a == 3 or a == 4 or a == 5:
        a = (random.randrange(0, 5))
        print(Fore.MAGENTA + a1[a])
    elif y == 1 or y == 2 or y == 3:
        y = (random.randrange(0, 2))
        print(Fore.LIGHTMAGENTA_EX + y1[y])
    elif x == 1 or x == 2:
        x = (random.randrange(0, 2))
        print(Fore.LIGHTRED_EX + x1[x])
    elif k == 0:
        k = (random.randrange(0, 24))
        print(Fore.LIGHTYELLOW_EX + Knife[k])
def action1():
    Revolution()
def action2():
    Recoil()
def action3():
    Nightmares()
def action4():
    Riptide()
def action5():
    Fracture()
def action6():
    Gamma2()
def action7():
    Gamma()
keyboard.add_hotkey('1', action1)
keyboard.add_hotkey('2', action2)
keyboard.add_hotkey('3', action3)
keyboard.add_hotkey('4', action4)
keyboard.add_hotkey('5', action5)
keyboard.add_hotkey('6', action6)
keyboard.add_hotkey('7', action7)

keyboard.wait('esc')