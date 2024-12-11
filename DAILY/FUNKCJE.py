# def wypiszListe(lista, rozmiar):
# 
    # for i in range(rozmiar):
# 
        # print(lista[i])
# 
# lista1 = [1,3,5,7,9]
# 
# lista2 = [1, 1]
# 
# wypiszListe(lista1,len(lista1))
# 
# wypiszListe(lista2,len(lista2))

# def nazwaFunkcji():
#                               TEORIA
#   ciało funkcji





# def DodajDwieLiczby(a,b):
    # wynik = a + b
    # return wynik



# Na początku musimy podać słowo kluczowe def.
# 
# Następnie podajemy nazwę funkcji. Nazwa funkcji to ciąg znaków. Bez spacji pomiędzy znakami.
# 
# Trzecia część funkcji to informacja o parametrach jakie funkcja przyjmuje. Listę wszystkich parametrów umieszczamy wewnątrz nawiasów okrągłych. Każdy parametr jest oddzielony od następnego przecinkiem. Jeśli funkcja nie przyjmuje żadnych parametrów to wewnątrz nawiasów okrągłych niczego nie umieszczamy.
# 
# Jak widzimy w powyższym przykładzie nazwa funkcji to: dodajDwieLiczby. Funkcja ta ma dwa parametry. Wywołując ją będziemy musieli podać dwie liczby typu.
# 
# Po nagłówku funkcji znajduje się tzw. ciało funkcji. Jest to nic innego jak blok instrukcji stanowiący naszą funkcję.
# 
# W ciele funkcji możemy deklarować nowe zmienne, ale są one widoczne tylko w obrębie tej funkcji. 

# 
# def dodajDwieLiczby(a, b):
# 
    # wynik = a + b
# 
    # return wynik
# 
# print("Podaj dwie Liczby:")
# 
# x = int(input())
# 
# y = int(input())
# 
# if dodajDwieLiczby(x,y) > 100:
# 
    # print("Suma podanych liczb jest większa od 100")
# 
# else:
# 
    # print("Suma podanych liczb jest mniejsza lub równa 100")
 

# def czyPelnoletni(wiek):
    # if wiek >= 18:
        # return True
    # else:
        # return False
    # 
# a = int(input("Podaj swój wiek: "))
# 
# if czyPelnoletni(a):
        # print("Jesteś pełnoletni")
# else:
        # print("Nie jesteś pełnoletni")
# 
# 
# def wypiszLiczby(a):
# 
    # if a<=0:
# 
        # return
# 
    # for i in range(a):
# 
        # print(i)
# 
    # return True
# 
# print("Podaj liczbę: ")
# x = int(input())
# 
# a = wypiszLiczby(x)
# 
# if a is None:
    # print("Żadna liczba nie została wpisana")



# Podsumowując sposób przekazywania argumentów przez wartość:
# 
# - Zmienna przekazana do funkcji jest jej kopią.
# 
# - Wszelkie operacje odbywają się na kopii, więc nie są widoczne poza blokiem funkcji.
# 
# - Zwracanie wartości z funkcji odbywa się za pomocą instrukcji return … ; Po instrukcji return podajemy konkretną wartość lub nazwę zmiennej.
# 
# - Jeżeli funkcja nie zwraca żadnej wartości, to po instrukcji return nic się nie pojawia
# 
# - W ciele funkcji może wystąpić więcej niż jedna instrukcja return.



# def wypiszListe(lst): 
# 
    # for i in lst:
# 
        # print(i)
# 
    # lst[0]=100
# 
# lista = [2,4,6,8]
# 
# wypiszListe(lista)
# 
# for i in lista:
# 
    # print(i)




# def f1():
# 
    # x=10
# 
    # print(x)
# 
# def f2():
# 
    # x=20
# 
    # print(x)
# 
# x=30
# 
# print(x)
# 
# f1()
# 
# f2()
# 
# print(x)
# 


# Jeśli np. z funkcji f2 usuniemy zmienną x i uruchomimy nasz program to zostaną wypisane następujące liczby:
# 30, 10, 30, 30
# Widzimy, że w tym przypadku została wypisana wartość 30,
# czyli wartość zmiennej zadeklarowanej w głównej części programu.




# Możemy tworzyć tzw. Zmienne globalne. 
# Zmienne globalne muszą być zadeklarowane z poprzedzającym je słowem kluczowym global
# def f1():
    # global x
    # x = 15
    # print(x)
# def f2():
    # print(x)
# 
# x = 40
# print(x)
# 
# f1()
# f2()
# print(x)

# Definicja funkcji 
# def make_and_eat_hamburger():
    # Ciało funkcji
    # print("Podsmaż mięso")
    # print("Podsmaż bułkę")
    # print("Dodaj pomidora")
    # print("Zjedz hamburgera")

# print("Wstań z łóżka")
# print("Umyj zęby")
# make_and_eat_hamburger()  # Użycie funkcji
# print("Pracuj")
# make_and_eat_hamburger()  # Użycie funkcji
# print("Pracuj")
# make_and_eat_hamburger()  # Użycie funkcji
# print("Graj w gry")
# print("Idź spać")



def silnia(n):

    if n <= 1:

        return 1

    else:

        return n * silnia( n - 1 )

print("Podaj liczbę")

a = int(input())

w=silnia(a)

print("wynik =",w)














