import zad4 as zad
import random
import matplotlib.pyplot as plt
import numpy as np

def lista_dyskow(n, a, b, r):
    '''
    Funkcja zwracajaca liste n dyskow
    :param n: ilość dysków
    :param a: minimalna dlugosc osi x i y
    :param b: maksymalna dlugosc osi x i y
    :param r: promien dyskow
    :return: lista n dyskow
    '''
    dyski=[]
    i=0
    if a == 0:
        while i<n:
            dyski.append((random.uniform(a+r, b-np.sign(b)*r),
                          random.uniform(a+r, b-np.sign(b)*r), r))
            i+=1
    elif b == 0:
        while i<n:
            dyski.append((random.uniform(a-np.sign(a)*r, b-r),
                          random.uniform(a-np.sign(a)*r, b-r), r))
            i+=1
    else:
        while i<n:
            dyski.append((random.uniform(a-np.sign(a)*r, b-np.sign(b)*r),
                          random.uniform(a-np.sign(a)*r, b-np.sign(b)*r), r))
            i+=1
    return dyski

x = lista_dyskow(100, -15, 15, 0.5)


def wykres_dyski(lista, x, a, b):
    '''
    Funkcja rysujaca wykres skladajacy sie z dyskow na plaszczyznie
    :param lista: lista dyskow
    :param x: kolor dyskow
    :param a: minimalna dlugosc osi x i y
    :param b: maksymalna dlugosc osi x i y
    :return: wykres dyskow
    '''
    plt.figure(figsize=(9, 9))
    for i in lista:
        circle1 = plt.Circle((i[0], i[1]), i[2], color=x, fill=False)
        plt.gcf().gca().add_artist(circle1)
    plt.grid(True)
    plt.axis([a, b, a, b])
    plt.show()

wykres_dyski(x, 'r', -15, 15)

def zmiana(lista, a, b, r):
    '''
    Funkcja szukajaca dysku ktory nie jest w kolizji z zadnym z listy
    :param lista: lista dyskow
    :param a: minimalna dlugosc osi x i y
    :param b: maksymalna dlugosc osi x i y
    :param r: promien dysku
    :return: dysk
    '''
    lista_true=[]
    while True not in lista_true:
        lista_t = []
        if a == 0:
            dysk = (random.uniform(a+r, b-np.sign(b)*r),
                          random.uniform(a+r, b-np.sign(b)*r), r)
        elif b == 0:
            dysk = (random.uniform(a-np.sign(a)*r, b-r),
                          random.uniform(a-np.sign(a)*r, b-r), r)
        else:
            dysk = (random.uniform(a-np.sign(a)*r, b-np.sign(b)*r),
                          random.uniform(a-np.sign(a)*r, b-np.sign(b)*r), r)
        for i in lista:
            a = zad.kolizja(dysk, i)
            lista_t.append(a)
        if True in lista_t:
            lista_true.append(False)
        else:
            lista_true.append(True)
    return dysk


def przesuniecie(lista, a, b, r):
    '''
    Funkcja zwracajaca liste dyskow bez kolizji
    :param lista: lista dyskow
    :param a: minimalna dlugosc osi x i y
    :param b: maksymalna dlugosc osi x i y
    :param r: promien zamienianych dyskow
    :return: lista dyskow bez kolizji
    '''
    for i in lista:
        for j in lista:
            if i != j and zad.kolizja(i, j) == True:
                k = zmiana(lista, a, b, r)
                lista[lista.index(i)] = k
                break
    return lista

y = przesuniecie(x, -15, 15, 0.5)
wykres_dyski(y, 'g', -15, 15)