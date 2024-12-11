# a = 1
# while a <= 3:
    # print("*")
    # a = a + 1


# i = 1
# while i < 10:
    # j = 1
    # while j < 5:
        # j = j + 2
        # i = i + 3
        # print(i)
        # print(j)


# print("Podaj wpłacaną kwotę: ")
# kwota = float(input())
# 
# i = 0
# while kwota < 0:
    # print("Popraw wpłacaną kwotę: ")
    # a = float(input())
    # print("Podano prawidłową kwotę")
    # break


# a = 0
# while a <5:
    # a = a + 1
    # if a == 3:
        # continue
    # print(a)



# 
# for i in range(23):   #program zawsze zaczyna wypisywać od zera
    # print(i)

# for a in range(0,100): #program zaczyna wypisywać cyfry od 0 do 99
    # print(a)

# for a in range(10,2,-2):  #DLACZEGO TO NIE DZIAŁA?
    # print(a)


# pierwsze = [2,3,5,7]   ## PĘTLA FOR IN RANGE
# for pierwsza in pierwsze:
    # print pierwsza
# 
# for a in range(5):
    # print(a)
# 
# else:
    # print("For-else a =",a)
# 
# for i in range(5):
#                                     #DLACZEGO TO NIE DZIAŁA?
    # print(i)
# 
# else:
# 
    # print("For-else i =",i)


#ZADANIE
#Napisz program wypisujący 20 kolejnych liczb parzystych, 
# począwszy od liczby podanej przez użytkownika. Użyj do tego pętli for.
# Pierwsza liczba podana do funkcji range oznacza liczbę od której rozpoczynamy wykonywanie pętli. 
# Druga liczba, to liczba po której osiągnięciu kończymy wykonywanie pętli. 
# Trzecia liczba określa o ile mają się zmieniać wartości w pętli.
 
print("Wprowadź liczbę: ")
a = int(input())
a += a % 2 # naprowadzenie na liczbę parzystą a + reszta z dzielenia przez 2 / += jest równoznaczne z a + ___
for b in range(5):
   print(a + 2 * b)


# ZADANIE
# Napisz program wczytujący liczby podawane przez użytkownika z klawiatury i kończący się w momencie, 
# kiedy suma wszystkich podanych liczb przekroczy 100. Wykorzystaj w programie pętlę while.




