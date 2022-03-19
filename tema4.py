##1.Avand lista masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel'] .

# 1. Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’
# 2. Faceti acelasi lucru cu un for each
# 3. Faceti acelasi lucru cu un while

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for i in range (len(masini)): #note to self:  preia dupa index
      print(f'Masina mea preferata este {masini[i]}')
for masina in masini: # preia dupa valoare
        print(f'Masina mea preferata este {masina}')
i=0
x = len(masini)
while i < x:
    masina=masini[i]
    print(f'Masina mea preferata este {masini[i]}')
    i+=1
else:
    print(f'Nu mai am masini preferate')


# #2.Aceeasi lista Folositi un for else
# #In for
# #   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# #In else
# #  Printati lista

for i in range(1,len(masini)-1):
    masini[i]=masini[i].upper()# scriem cu majuscule
else:
    print(masini)

# 3. Aceeasi lista, Vine un cumparator care doreste sa cumpere un Mercedes. Iterati prin ea prin modalitatea aleasa de voi
# Daca masina e mercedes
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam
# print(masini)


for masina in masini:
    if masina == 'Mercedes':
        print('Am gasit masina pe care o doriti')# ok, am gasit masina. imi itereaza codul pana la indexul anterior unde gaseste ce caut
        break# iese din ciclu
    else:
        print(f'Am gasit masina {masina} . Mai cautam')# cand mercedes nu e in lista, imi itereaza codul prin lungimea listei apoi printeaza ultimul mesaj dar doar ultimul item din lista ""


# 4.Aceasi lista Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun
# Iterati prin lista
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# (nu trebuie else)
# Printati S-ar putea sa va placa masina x
for masina in masini:
    if masina== 'Trabant' or masina== 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

# 5. Modernizati parcul de masini. Creati o lista goala, masini_vechi. Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# * Salvati aceste masini in masini_vechi
# * Suprascrieti-le cu ‘Tesla’.# Printati Modele vechi: x
# # Modele noi: x
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for i in range(len(masini)):
    if masini[i] == 'Lastun' or masini[i] == 'Trabant':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
else:
    print(f'Modele vechi: {masini_vechi}')
    print(f'Masini noi {masini}')



# 6.Avand dict pret_masini = {'Dacia': 6800, 'Lastun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
#Vine un client cu un buget de 15000 euro.Prezentati doar masinile care se incadreaza in acest buget
#Iterati prin dict.items() si accesati masina si pretul. Printati Pentru un buget de sub 15000 euro puteti alege masina x


pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget = 15000
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'Pentru un buget de sub 15000 euro puteti alege masina {masina} cu pretul {pret}')

# 7.Avand lista numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3] Iterati prin ea, Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
counter = 0
for numar in numere:
    if numar == 3:
        counter+=1
print(f'Numarul 3 apare de {counter}  ori')


# 8.Aceeasi lista, Iterati prin ea. Calculati si afisati suma numerelor (nu aveti voie sa folositi sum)
s=0
for numar in numere:
    s = s + numar
print(f'Suma numerelor din lista este {s}')

# 9.Aceeasi lista. Iterati prin ea. Afisati cel mai mare numar. (nu aveti voie sa folositi max)
for numar in numere:
    numere.sort()# sortare default crescatoare
print(f'cel mai mare numar este {numere[len(numere)-1]}')
max = numere[0]
for numar in numere:
    if numar > max:
        max = numar
print(max)

# 10.Aceeasi lista. Iterati prin ea.Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
#Ex: daca e 3, sa devina -3. Afisati noua lista
for i in range(len(numere)):
    if numere[i]> 0:
        numere[i] = numere[i]*-1
print(f' noua lista este : {numere}')

#c. Optionale (may need google)
# # 11. alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in range(len(alte_numere)):
    if alte_numere[i]%2 == 0:
        numere_pare.append(alte_numere[i])
        #print(numere_pare)
    if alte_numere[i]%2!=0:
        numere_impare.append(alte_numere[i])
        #print(numere_impare)
    if alte_numere[i]>0:
        numere_pozitive.append(alte_numere[i])
        #print(numere_pozitive)
    else:
        numere_negative.append(alte_numere[i])
        #print(numere_negative)
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

#12.Aceeasi lista. Ordonati crescator lista fara sa folositi sort. Va puteti inspira vizual de aici
# #https://www.youtube.com/watch?v=lyZQPjUT5B4
def bubblesort(alte_numere):
    for n in range(len(alte_numere) - 1, 0, -1):
        for i in range(n):
            if alte_numere[i] > alte_numere[i + 1]:
                #daca nr mai mic este cel din  indexul inferior, li se schimba pozitia in lista
                alte_numere[i], alte_numere[i + 1] = alte_numere[i + 1], alte_numere[i]

print(alte_numere)
bubblesort(alte_numere)
print(f'lista consecutiva e   {alte_numere}')
# asa fabricam noi o functie? foarte misto de inteles prin prisma dansului




#13.  Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# * Nr secret e mai mare
# * Nr secret e mai mic
# * Felicitari! Ai ghicit!

import random
numar_secret = random.randint(1,30)
numar_ghicit = None
while  numar_ghicit!= numar_secret:
    numar_ghicit= int(input('numarul din intervalul 1-30 ales de tine este: '))
    if numar_secret > numar_ghicit:
        print(f'Nr secret e mai mare')#numarul din intervalul 1-30 ales de tine este: 2. nr secret e 9. Nr secret e mai mare
    if numar_secret < numar_ghicit:
        print(f'Nr secret e mai mic')#numarul din intervalul 1-30 ales de tine este: 14. nr secret e 9. Nr secret e mai mic
else:
    print( f'Felicitari! Ai ghicit!')

# 14. Alegeti un numar de la tastatura
# Ex:7
# Scrieti un program care sa genereze in consola urmatoarea piramida
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# Ex:3
# 1
# 22
# # # 333



n = int(input('alege un nr de randuri: '))
for i in range(0,n+1):
    print(str(i) * (i))# varianta 1
for i in range (1, n + 1): # loop pt randuri. # varianta 2
    for j in range(i): # loop pt coloane
        print(i, end = " " )
    print()


# # 15. # Iterati prin lista 2d
# # # Printati ‘Cifra curenta este x’
# # # (hint: nested for - adica for in for)
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
for i in tastatura_telefon:
    for taste in i:
        print(f'Cifra curenta este : {taste}')