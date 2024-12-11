#ZADANIE
#Napisz program wypisujący 20 kolejnych liczb parzystych, 
# począwszy od liczby podanej przez użytkownika. Użyj do tego pętli for.
# Pierwsza liczba podana do funkcji range oznacza liczbę od której rozpoczynamy wykonywanie
# Druga liczba, to liczba po której osiągnięciu kończymy wykonywanie pętli. 
# Trzecia liczba określa o ile mają się zmieniać wartości w pętli.
 
# print("Wprowadź liczbę: ")
# a = int(input())
# a += a % 2 # naprowadzenie na liczbę parzystą a + reszta z dzielenia przez 2 / += jest równ
# for b in range(5):
#    print(a + 2 * b)


# ZADANIE
# Napisz program wczytujący liczby podawane przez użytkownika z klawiatury i kończący się w
# kiedy suma wszystkich podanych liczb przekroczy 100. Wykorzystaj w programie pętlę while.


# Napisz program który będzie wykonywał 4 podstawowe operacje arytmetyczne: +,

#Po wprowadzeniu dwóch liczb, 
# użytkownik ma wybrać lub wprowadzić rodzaj operacji jaka ma zostać wykonana.

# 
# W programie ocena.py zmodyfikujmy kod tak, 
# 
    # 90 punktów lub więcej odpowiada ocenie 
    # 80-89 punktów odpowiada ocenie 4
    # 70-79 punktów odpowiada ocenie 3
    # 65-69 punktów odpowiada ocenie 2
    # 64 punktów lub mniej odpowiada ocenie 1

#Napisz program który wczyta dwie liczby wprowadzone przez użytkownika.
#  Następnie wykonaj operacje: dodawania, odejmowania, mnożenie, dzielenie


# ZADANE
# ROZWIŃ POWYŻSZY PROGRAM PYTAJĄC UŻYTKOWNIKA
# O IMIĘ, NAZWISKO ORAZ WIEK I WYŚWIETLAJĄC TE INFORMACJE W NASTĘPUJĄCY SPOSÓB:

# Imię: Emilia
# Nazwisko: Darmos
# Wiek: 24


# Napisz program, który wypełni listę o rozmiarze 20, liczbami podanymi przez użytkownika.
# Następnie program powinien poprosić użytkownika o podanie liczby która będzie szukana. 
# W pętli for sprawdź i wypisz ile razy podana liczba występuje w tablicy.


# Rysunek przedstawia układ współrzędnych z numeracją ćwiartek tego układu. Ćwiartka numer jeden znajduje się u góry po prawej stronie. Ćwiartka numer dwa znajduje się u góry po lewej stronie. Ćwiartka numer trzy znajduje się na dole po lewej stronie. Ćwiartka numer cztery znajduje się na dole po prawej stronie.

# Napisz program zawierający funkcję:

# ktoraCwiartka(x, y)

# która dla punktu o współrzędnych (x, y) zwróci wartość 1..4, 
# identyfikującą jedną z ćwiartek układu współrzędnych 
# wewnątrz której leży ten punkt. 
# W przypadku, gdy punkt leży na którejkolwiek 
# osi współrzędnych funkcja powinna zwrócić 0.  

# Program prosi użytkownika o podanie współrzędnych, 
# wywołuje funkcję i wypisuje na ekranie numer zwrócony przez funkcję, 
# czyli numer ćwiartki układu.


# Napisz program przechowujący podawane przez użytkownika 
# dane osobowe (imię i nazwisko) w pliku

# Program powinien posiadać menu z następującymi opcjami:

#     Dodaj osobę (Użytkownik podaje imię, nazwisko. Dodajemy osobę na końcu listy)
#     Usuń osobę po numerze (Jeśli użytkownik poda np. 2 to usuwamy drugą osobę z naszej listy, 
# jak poda 3 to trzecią osobę itd. Jeśli na liście są 4 osoby a użytkownik poda np 7, to wypisujemy komunikat np: Nie ma takiej osoby)
#     Usuń osobę o podanym imieniu i nazwisku (Użytkownik podaje z klawiatury imię i nazwisko, program usuwa wszystkie osoby o podanym imieniu i nazwisku).
#     Wypisz osoby (Wypisujemy dane wszystkich osób przechowywanych na liście)
#     Zapisz dane (Zapisujemy do pliku dane wszystkich osób)
#     Wczytaj dane (Usuwany wszystkie osoby z listy, następnie odczytujemy z pliku dane osób i dodajemy je do listy) 

# Program ma na początku wyświetlać menu z opisanymi wyżej opcjami. Po wybraniu danej opcji program wykonuje daną operację i ponownie wypisuje menu.

import os
if os.path.exists("warunki.py"): # sprawdź, czy istnieje plik plik.txt
    print("Plik \"warunki.py\" istnieje i jest gotowy do pracy")
else:
    print("Plik pod wskazaną ścieżką nie istnieje")