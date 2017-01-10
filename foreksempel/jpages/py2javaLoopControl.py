# for-l�kke eksempel 1: intro til for-l�kke
for i in range(10):
    print(i)


# for-l�kke eksempel 2: �ke telleren med mer enn 1
print("Alle tall i fem-gangen t.o.m. 30 er:")
for i in range(5, 30, 5):
    print(i)


# for-l�kke eksempel 3: andre ting enn integers og telling
# python-versjonen blir enklest som en while-l�kke
s = "X"
while s != "XXX":
    print("Alt er greit! Ordet er " + s)
    s += "X"


# for-l�kke eksempel 4: for-each l�kke
# skrive ut alle ord i en liste (Java: array)
prog_spraak = ["Python", "C++", "Java", "PHP"]
for spraak in prog_spraak:
    print(spraak)


# for-l�kke eksempel 5: bruke liste-lengden
# g� gjennom liste, og ha en teller (i)
personer = ["Cecilie", "Vegard", "Vemund", "Nils", "Ragnar"]
for i in range( len(personer) ):
    print(personer[i] + " er p� plass " + str(i+1))


# for-l�kke eksempel 6: break
# brukes helt likt i while-l�kker
# lete gjennom en liste helt til vi finner Gl�shaugen
plasser = ["Dragvoll", "St. Olav", "Tunga", "Kalvskinnet", "Gl�shaugen", "Gj�vik"]
print("Leter etter Gl�shaugen")
for plass in plasser:
    if plass == "Gl�shaugen":
        break
    print("Leter fremdeles... er p� " + plass + " n�.")
print("Jeg fant!")


# for-l�kke eksempel 7: nestede l�kker
# bruker array, for intro se liste- TODO
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print('Her er alle rutene i et sjakkbrett:')
for i in range(8):
    for j in range(8):
        print(letters[i] + str(j+1))
        

# while-l�kke eksempel 1: intro til while-l�kke
timer = 5
while timer > 0:
    print("Tid igjen: " + str(timer))
    timer -= 1
print("Tiden er ute!")



# while-l�kke eksempel 2: uendelig l�kke, med break
# brukes stort sett bare med input e.l., men det dropper vi her
# s� eksempelet er bare � skrive ut noe helt til vi har gjort det 3 ganger
# bare for � illustrere uendelige l�kker
teller = 0
while (True):
    print("Java er best, ingen protest!")
    teller += 1
    if teller == 3: 
        break
