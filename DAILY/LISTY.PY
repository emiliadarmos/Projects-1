# numbers = []
# for i in range(5):
    # print("Podaj liczbę: ")
    # numbers.append(int(input()))   #append - dodaje obiekt do listy
# 
    # for i in range(len(numbers)):
        # print(numbers[i])


# oceny = []
# 
# for i in range(5):
# 
    # print("Wprowadź ocenę:")
# 
    # oceny.append(int(input()))
# 
# print("Otrzymałeś następujące oceny:")
# 
# suma = 0.0
# 
# for i in range(len(oceny)):
# 
    # print(oceny[i])
# 
    # suma = suma + oceny[i]
# 
# print("Twoja średnia to:",suma/len(oceny))


# 
# list = [1,3,5,7]
# print("Rozmiar listy: ", len(list))

# 
# lista3 = ["aa", 1, 2.5]
# 
# for i in range(len(lista3)):
# 
    # print(lista3[i])
# 
# lista4 = [ ["aa", "bb"],  [1, 2.5] ]
# 
# for i in range(len(lista4)):           #dwie listy 
# 
    # for j in range(len(lista4[i])):
# 
        # print(lista4[i][j])

# lista = [1,2,3]
# lista.append(4)
# 
# for i in range(len(lista)):   #for in range wypisze liczby w dół, zwykłe print wypisze liczby w jednej linii
    # print(lista[i])           # dodajemy len żeby program wypisał daną listę




# lista1 = [3,4,5]
# lista1.insert(3,6)
# for i in range(len(lista1)):
    # print(lista1[i])

# Metoda insert dołącza nowy element na podanej pozycji, przesuwając istniejące elementy.
# Pierwszy argument tej metody to pozycja na której dodajemy, drugi argument to dodawany element.




# lista = [1,2,3,4]
# del(lista[2])
# print(lista)


# Jeśli chcemy usunąć określony element z listy,
# to wywołujemy instrukcję del podając nazwę oraz index usuwanego elementu

# lista = [7,8,3,5]
# lista.sort()
# 
# for i in range(len(lista)):
    # print(lista[i])
# 
# lista.reverse()
# print(lista)


lista = [4,7,9,1,2]

print(4 in lista)

print(5 in lista)

print(4 not in lista)

print(5 not in lista)



# W celu sprawdzenia czy lista zawiera określony element możemy wywołać operatory in lub not in
# 
# Operator in zwraca True jeśli lista zawiera określony element w przeciwnym wypadku zwraca False.
# 
# Operator not in zwraca True jeśli lista nie zawiera określonego elementu w przeciwnym wypadku zwraca False.