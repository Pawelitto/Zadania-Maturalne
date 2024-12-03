# Plik skrot.txt zawiera 200 dodatnich liczb całkowitych, mniejszych od 30 000. Każda
# liczba jest zapisana w osobnym wierszu. Dla co najmniej jednej z tych liczb nie istnieje
# nieparzysty skrót.

# Napisz program, który wyznaczy liczbę wszystkich liczb z pliku skrot.txt, dla których
# nie istnieje nieparzysty skrót, oraz poda największą z nich. Odpowiedź zapisz w pliku
# wyniki3_2.txt.

# Plik skrot_przyklad.txt zawiera 20 liczb mniejszych od 30 000. Dla danych
# zawartych w pliku skrot_przyklad.txt prawidłową odpowiedzią jest:
# 2
# 2428
# (w pliku są dwie liczby, dla których nie istnieje nieparzysty skrót: 266 i 2428; 2428 jest
# największą z nich).

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

with open("Dane-NF-2405/skrot_przyklad.txt", "r") as file:
    numbers = [int(line) for line in file.readlines()]

combined_numbers = [number for number in numbers if nieparzysty_skrot(number) == 0]

print(len(combined_numbers))
print(max(combined_numbers))
