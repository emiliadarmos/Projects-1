
# Napisz program który będzie wykonywał 4 podstawowe operacje arytmetyczne: +,-,*,/

#Po wprowadzeniu dwóch liczb, 
# użytkownik ma wybrać lub wprowadzić rodzaj operacji jaka ma zostać wykonana.


print("Podaj pierwszą liczbę: ")
a = int(input())

print("Podaj drugą liczbę: ")
b = int(input())

print("Wybierz rodzaj działania: +, -, *, /")
c = input()

if c == "+":
    print("Wynik to: ")
    print(a + b)
if c == "-":
    print("Wynik to: ")
    print(a - b)
if c == "*":
    print("Wynik to: ")
    print(a * b)
if c == "/":
    print("Wynik to: ")
    print(a / b)

else:
    print("Nie ma takiego działania!")



