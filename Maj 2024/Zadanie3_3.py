# Plik skrot2.txt zawiera 200 dodatnich liczb całkowitych, mniejszych od 30 000. Każda
# liczba jest zapisana w osobnym wierszu. Dla każdej z tych liczb istnieje nieparzysty
# skrót.

# Napisz program, który wypisze te liczby z pliku skrot2.txt, dla których największy
# wspólny dzielnik liczby i jej nieparzystego skrótu jest równy 7. Odpowiedź zapisz w pliku
# wyniki3_3.txt. Twój program powinien wypisać w każdym wierszu wyniku po jednej
# liczbie z pliku skrot2.txt, dla której jest spełniony powyższy warunek.

# Plik skrot2_przyklad.txt zawiera 20 liczb spełniających warunki zadania. Dla danych
# zawartych w pliku skrot2_przyklad.txt prawidłową odpowiedzią jest:
# 4872
# 23527

def nieparzysty_skrot(n):
    m = 0
    mnoznik = 1

    while n > 0:
        ostatnia = n % 10
        if ostatnia % 2 != 0:
            m += ostatnia * mnoznik
            mnoznik = mnoznik * 10

        n //= 10
    return m

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

with open("Dane-NF-2405/skrot2_przyklad.txt", "r") as file:
    numbers = [int(line) for line in file.readlines()]

combined_numbers = [number for number in numbers if nwd(nieparzysty_skrot(number), number) == 7]
print(combined_numbers)