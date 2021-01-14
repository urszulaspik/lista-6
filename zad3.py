def przesuniecie(dysk, wektor):
    '''
    Funkcja przesuwa dysk o podany wektor
    :param dysk: krotka skladajaca sie z 3 liczb, 2 pierwsze to wspolrzedne srodka a 3 to promien
    :param wektor: krotka skladajaca sie z 3 liczb, 2 pierwsze to wspolrzedne srodka a 3 to promien
    :return: nowe wspolrzedne dysku
    '''
    if type(dysk) == tuple and type(wektor) == tuple and len(dysk) == 3 and len(wektor) == 2 and dysk[2] > 0:
        nowy_dysk = (dysk[0] + wektor[0], dysk[1] + wektor[1], dysk[2])
        return nowy_dysk
    else:
        return 'Błędne dane'

print(przesuniecie((1, 2, 3), (-1, 2)))