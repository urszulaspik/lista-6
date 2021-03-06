import math


def kolizja(dysk1, dysk2):
    '''
    Funkcja wykrywa kolizje miedzy dwoma dyskami
    :param dysk1: krotka skladajaca sie z 3 liczb, 2 pierwsze to wspolrzedne srodka a 3 to promien
    :param dysk2: krotka skladajaca sie z 3 liczb, 2 pierwsze to wspolrzedne srodka a 3 to promien
    :return: True - dyski zachodza na siebie, False - nie zachodza
    '''
    if type(dysk1) == tuple and type(dysk2) == tuple and len(dysk1) == 3 and len(dysk2) == 3:
        if dysk1[2] > 0 and dysk2[2] > 0:
            odleglosc = math.sqrt((dysk2[0]-dysk1[0])**2 + (dysk2[1] - dysk1[1])**2)
            if odleglosc < (dysk1[2] + dysk2[2]):
                return True
            else:
                return False
        else:
            return 'Promień jest mniejszy od 0!'
    else:
        return 'Błędne dane'

print(kolizja((1, 2, 4), (2, 4, 6)))
