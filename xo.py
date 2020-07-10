from random import randint as rng

#Funkcja sprawdzająca czy dana koordynata jest już zajęta lub jest niepoprawna
def spr_lock(ekran, koord):
    try:
        if ekran[koord] == "x" or ekran[koord] == "o":
            return False
        else:
            return True
    except KeyError:
        return False

#Funkcja konwertująca dwa inputy ze strony gracza w jedną liczbę (np. 1 i 1 w 11)
def input_to_koord(inp1, inp2):
    ans = inp1 + inp2
    return int(ans)

#Funkcja która sprawdza czy nie ma trzech identycznych znaków w lini
def spr_win(ekran, gracze):
    if ekran[11] == ekran[12] == ekran[13] and ekran[11] != " ":
        znak = ekran[11]
    elif ekran[21] == ekran[22] == ekran[23] and ekran[21] != " ":
        znak = ekran[21]
    elif ekran[31] == ekran[32] == ekran[33] and ekran[31] != " ":
        znak = ekran[31]
    elif ekran[11] == ekran[21] == ekran[31] and ekran[11] != " ":
        znak = ekran[11]
    elif ekran[12] == ekran[22] == ekran[32] and ekran[12] != " ":
        znak = ekran[12]
    elif ekran[13] == ekran[23] == ekran[33] and ekran[13] != " ":
        znak = ekran[13]
    elif ekran[11] == ekran[22] == ekran[33] and ekran[11] != " ":
        znak = ekran[11]
    elif ekran[13] == ekran[22] == ekran[31] and ekran[13] != " ":
        znak = ekran[13]
    
    try:
        wygrany = gracze[znak]
        return wygrany
    except UnboundLocalError:
        return " "

#Funkcje odpowiadające za inteligencje przeciwnika
def int_los(znak_komp):
    while True:
        koord_komp = input_to_koord(str(rng(1,3)), str(rng(1,3)))
        if ekran[koord_komp] == "x" or ekran[koord_komp] == "o":
            continue
        else:
            ekran[koord_komp] = znak_komp
            break

def int_atak(ekran, znak_komp, znak_gracz):
    while True:
    #1
        if znak_komp == ekran[11] == ekran[12]:
            if spr_lock(ekran, 13) == True:
                ekran[13] = znak_komp
                break                
        if znak_komp == ekran[11] == ekran[13]:
            if spr_lock(ekran, 12) == True:
                ekran[12] = znak_komp
                break    
        if znak_komp == ekran[12] == ekran[13]:
            if spr_lock(ekran, 11) == True:
                ekran[11] = znak_komp
                break  
        #2
        if znak_komp == ekran[21] == ekran[22]:
            if spr_lock(ekran, 23) == True:
                ekran[23] = znak_komp
                break  
        if znak_komp == ekran[21] == ekran[23]:
            if spr_lock(ekran, 22) == True:
                ekran[22] = znak_komp
                break 
        if znak_komp == ekran[23] == ekran[22]:
            if spr_lock(ekran, 21) == True:
                ekran[21] = znak_komp
                break 
        #3
        if znak_komp == ekran[31] == ekran[32]:
            if spr_lock(ekran, 33) == True:
                ekran[33] = znak_komp
                break
        if znak_komp == ekran[31] == ekran[33]:
            if spr_lock(ekran, 32) == True:
                ekran[32] = znak_komp
                break
        if znak_komp == ekran[33] == ekran[32]:
            if spr_lock(ekran, 31) == True:
                ekran[31] = znak_komp
                break
        #4
        if znak_komp == ekran[11] == ekran[22]:
            if spr_lock(ekran, 33) == True:
                ekran[33] = znak_komp
                break
        if znak_komp == ekran[11] == ekran[33]:
            if spr_lock(ekran, 22) == True:
                ekran[22] = znak_komp
                break
        if znak_komp == ekran[22] == ekran[33]:
            if spr_lock(ekran, 11) == True:
                ekran[11] = znak_komp
                break 
        #5
        if znak_komp == ekran[13] == ekran[22]:
            if spr_lock(ekran, 31) == True:
                ekran[31] = znak_komp
                break
        if znak_komp == ekran[13] == ekran[31]:
            if spr_lock(ekran, 22) == True:
                ekran[22] = znak_komp
                break
        if znak_komp == ekran[31] == ekran[22]:
            if spr_lock(ekran, 13) == True:
                ekran[13] = znak_komp
                break
        #6
        if znak_komp == ekran[11] == ekran[21]:
            if spr_lock(ekran, 31) == True:
                ekran[31] = znak_komp
                break
        if znak_komp == ekran[31] == ekran[21]:
            if spr_lock(ekran, 11) == True:
                ekran[11] = znak_komp
                break
        if znak_komp == ekran[11] == ekran[31]:
            if spr_lock(ekran, 21) == True:
                ekran[21] = znak_komp
                break
        #7
        if znak_komp == ekran[12] == ekran[22]:
            if spr_lock(ekran, 32) == True:
                ekran[32] = znak_komp
                break
        if znak_komp == ekran[22] == ekran[32]:
            if spr_lock(ekran, 12) == True:
                ekran[12] = znak_komp
                break
        if znak_komp == ekran[32] == ekran[12]:
            if spr_lock(ekran, 22) == True:
                ekran[22] = znak_komp
                break
        #8
        if znak_komp == ekran[13] == ekran[23]:
            if spr_lock(ekran, 33) == True:
                ekran[33] = znak_komp
                break
        if znak_komp == ekran[13] == ekran[33]:
            if spr_lock(ekran, 23) == True:
                ekran[23] = znak_komp
                break
        if znak_komp == ekran[23] == ekran[33]:
            if spr_lock(ekran, 13) == True:
                ekran[13] = znak_komp
                break
        else:
            int_def(ekran, znak_komp, znak_gracz)
            break
        
def int_def(ekran, znak_komp, znak_gracz):
    while True:
    #1
        if znak_gracz == ekran[11] == ekran[12]:
            if spr_lock(ekran, 13) == True:
                ekran[13] = znak_komp
                break    
        if znak_gracz == ekran[11] == ekran[13]:
            if spr_lock(ekran, 12) == True:
                ekran[12] = znak_komp
                break
        if znak_gracz == ekran[12] == ekran[13]:
            if spr_lock(ekran, 11) == True:
                ekran[11] = znak_komp
                break
        #2
        if znak_gracz == ekran[21] == ekran[22]:
            if spr_lock(ekran, 23) == True:
                ekran[23] = znak_komp
                break
        if znak_gracz == ekran[21] == ekran[23]:
            if spr_lock(ekran, 22) == True:
                ekran[22] = znak_komp
                break
        if znak_gracz == ekran[23] == ekran[22]:
            if spr_lock(ekran, 21) == True:
                ekran[21] = znak_komp
                break 
        #3
        if znak_gracz == ekran[31] == ekran[32]:
            if spr_lock(ekran, 33) == True:
                ekran[33] = znak_komp
                break
        if znak_gracz == ekran[31] == ekran[33]:
            if spr_lock(ekran, 32) == True:
                ekran[32] = znak_komp
                break
        if znak_gracz == ekran[33] == ekran[32]:
            if spr_lock(ekran, 31) == True:
                ekran[31] = znak_komp
                break
        #4
        if znak_gracz == ekran[11] == ekran[22]:
            if spr_lock(ekran, 33) == True:
                ekran[33] = znak_komp
                break
        if znak_gracz == ekran[11] == ekran[33]:
            if spr_lock(ekran, 22) == True:
                ekran[22] = znak_komp
                break
        if znak_gracz == ekran[22] == ekran[33]:
            if spr_lock(ekran, 11) == True:
                ekran[11] = znak_komp
                break
        #5
        if znak_gracz == ekran[13] == ekran[22]:
            if spr_lock(ekran, 31) == True:
                ekran[31] = znak_komp
                break
        if znak_gracz == ekran[13] == ekran[31]:
            if spr_lock(ekran, 22) == True:
                ekran[22] = znak_komp
                break
        if znak_gracz == ekran[31] == ekran[22]:
            if spr_lock(ekran, 13) == True:
                ekran[13] = znak_komp
                break
        #6
        if znak_gracz == ekran[11] == ekran[21]:
            if spr_lock(ekran, 31) == True:
                ekran[31] = znak_komp
                break
        if znak_gracz == ekran[31] == ekran[21]:
            if spr_lock(ekran, 11) == True:
                ekran[11] = znak_komp
                break
        if znak_gracz == ekran[11] == ekran[31]:
            if spr_lock(ekran, 21) == True:
                ekran[21] = znak_komp
                break
        #7
        if znak_gracz == ekran[12] == ekran[22]:
            if spr_lock(ekran, 32) == True:
                ekran[32] = znak_komp
                break
        if znak_gracz == ekran[22] == ekran[32]:
            if spr_lock(ekran, 12) == True:
                ekran[12] = znak_komp
                break
        if znak_gracz == ekran[32] == ekran[12]:
            if spr_lock(ekran, 22) == True:
                ekran[22] = znak_komp
                break
        #8
        if znak_gracz == ekran[13] == ekran[23]:
            if spr_lock(ekran, 33) == True:
                ekran[33] = znak_komp
                break
        if znak_gracz == ekran[13] == ekran[33]:
            if spr_lock(ekran, 23) == True:
                ekran[23] = znak_komp
                break
        if znak_gracz == ekran[23] == ekran[33]:
            if spr_lock(ekran, 13) == True:
                ekran[13] = znak_komp
                break
        else:
            int_los(znak_komp)
            break

def inteligencja(ekran, znak_komp, znak_gracz):
    int_atak(ekran, znak_komp, znak_gracz)

#Słownik ekran do którego wpisujemy znaki
ekran = {11:" ", 12:" ", 13:" ", 21:" ", 22:" ", 23:" ", 31:" ", 32:" ", 33:" "}

#Wyświetlacz oparty o słownik "ekran"
def wyswietlacz():
    print("")
    print("   1 2 3")
    print("1 |" + ekran[11] + "|" + ekran[12] + "|" + ekran[13] + "|")
    print("2 |" + ekran[21] + "|" + ekran[22] + "|" + ekran[23] + "|")
    print("3 |" + ekran[31] + "|" + ekran[32] + "|" + ekran[33] + "|")
    print("")

#System wyboru znaku
print("")
while True:
    pyt = input("Wybierz znak 'x' lub 'o' ('x' zawsze zaczyna): ")
    if pyt == "x":
        znak_gracz = "x"
        znak_komp = "o"
        gracze = {"x":"Gracz", "o":"Komputer"}
        ruchy = 5
        break
    elif pyt == "o":
        znak_gracz = "o"
        znak_komp = "x"
        gracze = {"o":"Gracz", "x":"Komputer"}
        ruchy = 4
        break
    else:
        print("Odpowiedź nie zgodna z kluczem! Spróbuj ponownie.")
        continue
print("")

draw = True

#Silnik gry
try:
    while True:
        if ruchy == 5:
            wyswietlacz()
            for _ in range(4):
                while True:
                    koord = input_to_koord(input("Numer wiersza: "), input("Numer kolumny: "))
                    if spr_lock(ekran, koord) == True:
                        ekran[koord] = znak_gracz
                        break
                    else:
                        print("Pole jest zajęte lub podane koordynaty są niepoprawne! Spróbuj jeszcze raz.")
                        print("")
                        continue
                if spr_win(ekran, gracze) != " ":
                    winner = spr_win(ekran, gracze)
                    draw = False
                    assert 1 < 0
                inteligencja(ekran, znak_komp, znak_gracz)
                if spr_win(ekran, gracze) != " ":
                    winner = spr_win(ekran, gracze)
                    draw = False 
                    assert 1 < 0
                wyswietlacz()
            while True:
                koord = input_to_koord(input("Numer wiersza: "), input("Numer kolumny: "))
                if spr_lock(ekran, koord) == True:
                    ekran[koord] = znak_gracz
                    break
                else:
                    print("Pole jest zajęte lub podane koordynaty są niepoprawne! Spróbuj jeszcze raz.")
                    print("")
                    continue
            if spr_win(ekran, gracze) != " ":
                    winner = spr_win(ekran, gracze)
                    draw = False 
                    assert 1 < 0
            wyswietlacz()
            break
        elif ruchy == 4:
            for _ in range(4):
                inteligencja(ekran, znak_komp, znak_gracz)
                if spr_win(ekran, gracze) != " ":
                    winner = spr_win(ekran, gracze)
                    draw = False 
                    assert 1 < 0
                wyswietlacz()
                while True:
                    koord = input_to_koord(input("Numer wiersza: "), input("Numer kolumny: "))
                    if spr_lock(ekran, koord) == True:
                        ekran[koord] = znak_gracz
                        break
                    else:
                        print("Pole jest zajęte lub podane koordynaty są niepoprawne! Spróbuj jeszcze raz.")
                        print("")
                        continue
                if spr_win(ekran, gracze) != " ":
                    winner = spr_win(ekran, gracze)
                    draw = False 
                    assert 1 < 0
            inteligencja(ekran, znak_komp, znak_gracz)
            if spr_win(ekran, gracze) != " ":
                    winner = spr_win(ekran, gracze)
                    draw = False 
                    assert 1 < 0
            wyswietlacz()
            break
except AssertionError:
    x = "KONIEC" 

    
#Wyświetlenie wyniku
print("")
if draw == True:
    print("REMIS")
elif draw == False:
    wyswietlacz()
    print(winner + " WYGRAŁ")

print("")
end = input("Naciśnij ENTER, by zakończyć działanie programu.")
