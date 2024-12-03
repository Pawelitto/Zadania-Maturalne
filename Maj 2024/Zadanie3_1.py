# Nieparzystym skrótem dodatniej liczby całkowitej n nazwiemy dodatnią liczbę całkowitą m,
# która powstaje przez usunięcie cyfr parzystych z zapisu dziesiętnego liczby n.
# Nieparzysty skrót liczby całkowitej n nie istnieje, gdy jej zapis dziesiętny składa się tylko
# z cyfr parzystych.

# Przykład:
#  Nieparzystym skrótem liczby 294762 jest liczba 97.
#  Nieparzystym skrótem liczby 39101 jest liczba 3911.
#  Nieparzysty skrót liczby 224 nie istnieje.

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

print(nieparzysty_skrot(294762))
print(nieparzysty_skrot(39101))