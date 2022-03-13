# def suma(a,b):
#     return a+b
Tema5.py
Ieri
Vin. 18:40

Teodora Birle a încărcat un articol
Text
Tema5.py
'''Pentru toate exercitiile
Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
Daca functia are return, printati raspunsul
1. Functie care sa calculeze si sa returneze suma a 2 numere
'''
# cazul in care putem introduce numerele de la tastatura, e mai dinamic
x = int(input('Introdu primul numar: '))
y = int(input('Introdu al doilea numar: '))
def suma_numere(x,y):
    suma = x + y
    return (f'Suma celor doau numere este: {suma}')

print(suma_numere(x,y))

# cazul in care punem argumentele cand apelam functia
def suma_numere(a,b):
    suma = a + b
    return (f'Suma celor doau numere este: {suma}')

print(suma_numere(8,10))
print(suma_numere(78,10))

'''2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar'''
def par_impar(numar): # definim functia si-i punem parametrul numar
    if numar % 2 == 0: # verificam prin modulo daca este par
        return(f'{numar} este un numar par') # returnam un raspuns
    else:
        return(f'{numar} este un numar impar')

print(par_impar(84))
print(par_impar(75))
'''3. Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu) 
'''
def total_caractere(nume, prenume1, prenume2):
    total_string = (nume + prenume1 + prenume2)# punem parametrii intr-un string pt a-l putea parcurge
    total_string = total_string.replace(' ', '')# in cazul in care apar spatii, le eliminam
#   print(f'{total_string}')
    return len(total_string)# dimensiunea stringului ne va returna numarul de caractere

print(total_caractere('Birle', 'Dan ', 'Vasile'))
print(total_caractere('Pop', 'Victor', 'Stefan'))
print(total_caractere('Popescu    ', 'Alex', ' '))

'''4. Functie care returneaza aria dreptunghiului'''

# lungime_input = int(input('Introdu lungimea: '))
# latime_input = int(input('Introdu latimea: '))
def aria_dreptunghi(Lungime, latime):
    arie =  Lungime * latime
    return (f'Aria dreptunghiului este: {arie}')

print(aria_dreptunghi(8, 5))
print(aria_dreptunghi(10, 45))

'''5. Functie care returneaza aria cercului'''

PI = 3.14
def aria_cercului(raza):
    arie_cerc = raza * raza * PI
    return (f'Aria cercului este: {arie_cerc}')

print(aria_cercului(6))
print(aria_cercului(10))
'''6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu'''

string_input = 'abc12311 :&   ABCD1! '
x = input('Introduceti caracterul cautat: ')
def cautare_caracter(string, x):
    contine = False
    nr = 0
    for char in string:
        if char == x:
            contine = True
            nr = nr + 1
    print(f'{x} apare in string de {nr} ori')
    return contine

print(cautare_caracter(string_input, x))

'''7. Functie fara return, primeste un string si printeaza pe ecran:
Nr de caractere lower case este x
Nr de caractere upper case exte y '''

string_input = 'abc1ABCD!'
def lower_upper(string):
    char_upper = 0
    char_lower = 0
    for char in string:
        if char.isupper():
            char_upper = char_upper + 1
        elif char.islower():
            char_lower = char_lower + 1
        # else:
        #     print('nu ati introdus litere')
    print(f'Numarul de caractere mari este: {char_upper}')
    print(f'Numarul de caractere mici este: {char_lower}')

lower_upper(string_input)

'''8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive'''

lista_numere = [1, -4, 78, -5, 0, 85, 4, -10, -2]
lista_numere_pozitive = []

def numere_pozitive(numere):
    for numar in numere:
        if numar < 0:
            lista_numere_pozitive.append(numar)
    return(lista_numere_pozitive)

print(numere_pozitive(lista_numere))


'''9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale. '''

def doua_numere(x, y):
    if x == y:
        print(f'Numerele sunt egale' )
    elif x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    else:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')

doua_numere(89, -5)
doua_numere(7, 46)

'''10. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False'''

set_numere_input = {2, 5, 8 ,78, -8, 45}
def adaugare_numar(set_numere, numar_nou):
    if numar_nou in set_numere:
        print(f'nu am adaugat numarul {numar_nou} in set, exista deja')
        return False
    else:
        set_numere.add(numar_nou)
        print(f'am adaugat numarul {numar_nou} in set')
        print(set_numere)
        return True

print(adaugare_numar(set_numere_input, 78))
print(adaugare_numar(set_numere_input, 75))


'''c. Optionale (may need google)
11. Functie care primeste o luna din an si returneaza cate zile are acea luna'''

lunile_anului = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}
def calendar(luna):
    if luna in lunile_anului:
        return (lunile_anului.get(luna))

print(calendar('June'))
print(calendar('January'))
print(calendar('February'))

'''14. Functie care primeste 3 numere
Returneaza valoarea maxima dintre ele'''

def maxim(x, y, z):
    if x == y == z:
        return ('numerele sunt egale')
    elif x >= y and x >= z:
        return (f'{x} este cel mai mare numar')
    elif y >= x and y >= z:
        return (f'{y} este cel mai mare numar')
    else:
        return (f'{z} este cel mai mare numar')

print(maxim(20, 20, 2))
print(maxim(5, 100, 100))
print(maxim(7, 7, 7))
print(maxim(17, 2, 17))

'''BONUS:16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
'Numele este de baiat' sau 'Numele este de fata'
'''
exceptii_fete = ['Carmen', 'Iris', 'Damaris']
exceptii_baieti = ['Horea', 'Mihnea', 'Horea', 'Toma']

def verificare_nume(nume):
    if nume in exceptii_fete:
        return (f'Numele introdus este de fata')
    elif nume in exceptii_baieti:
        return(f'Numele introdus este de baiat')
    elif nume[len(nume)-1] == 'a':
        return (f'Numele introdus este de fata')
    else:
        return('Numele introdus este de baiat')

print(verificare_nume('Victor'))
print(verificare_nume('Horea'))
print(verificare_nume('Rodica'))
print(verificare_nume('Iris'))


Tema5.py
Săptămâna aceasta
Joi 17:14

Isabela Didraga a încărcat un articol
Text
Tema5.py
# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 5 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Functii din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 7 despre OOP din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
#
# Pentru toate exercitiile
# Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
# Daca functia are return, printati raspunsul
#
# b. Dificultate: usor spre mediu
#
# 1. Functie care sa calculeze si sa returneze suma a 2 numere
# def suma_Nr (a, b):
#     return a + b

# # verificare
# print(suma_Nr(4, 5))

# # 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
# def nr(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False

# # verificare
# raspuns1 = nr(2) #  => True
# raspuns2 = nr(7) #  => False
# print(raspuns1)
# print(raspuns2)

# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)
# def nr_total_caractere(nume, prenume, nume_mijlociu):
#      return len(nume) + len(prenume) + len(nume_mijlociu)
#
# # verificare
# print(nr_total_caractere('Didraga', 'Isabela', 'Raluca'))  # => 20

# 4. Functie care returneaza aria dreptunghiului
# def arie_dreptunghi(l,L):
#     return l * L
#
# # verificare
# print(arie_dreptunghi(3,4)) #  => 12

# 5. Functie care returneaza aria cercului
# PI = 3.14
# def arie_cerc(r):
#     return PI * r * r
#
# # verificare
# print(arie_cerc(4)) #  => 50.24

# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
# def caracter(my_string):
#     x = input('Alege un caracter: ')
#     if x in my_string:
#         return True
#     else:
#         return False
#
# # verificare
# print(caracter('Ana are mere')) #  => pt 'n' => True / pt 'P' => False

# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y
# def char_counter(my_string):
#     counter_lower = 0
#     counter_upper = 0
#     for i in range(len(my_string)):
#         if(my_string[i] >= 'a' and my_string[i] <= 'z'):
#             counter_lower += 1
#         elif(my_string[i] >= 'A' and my_string[i] <= 'Z'):
#             counter_upper += 1
#     print(f'Lower case letters: {counter_lower}')
#     print(f'Lower case letters: {counter_upper}')
# (char_counter('ABiku')) #  => 3 lowe si 2 upper

# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
#
# lista1 = [1, -2, -1, 2, 5, -9, 2]
# lista2 = []
# def lista_nr_pozitive(l1, l2):
#     for i in range(len(l1)):
#         if l1[i] > 0:
#             l2.append(l1[i])
#     return l2
#     print(f'Lista cu numere pozitive este: {l2}')
# print(lista_nr_pozitive(lista1, lista2))

# 9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.
#
# def comparare(a, b):
#     if a > b:
#         print(f'Numarul {a} este mai mare decat {b}.')
#     elif b > a:
#         print(f'Numarul {b} este mai mare decat {a}')
#     else:
#         print('Numerele sunt egale.')
# (comparare(2, 5))

# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
#
# def nr_set(nr, set):
#     if nr in set:
#         print('Nu am adaugat numarul in set. Acesta exista deja.')
#         return False
#     else:
#         set.add(nr)
#         print(f'Am adaugat numar nou in set: {set}')
#         return True
# nr_set(2,{1, 2, 3, 4}) #  #  pt 2, nu il adauga si pt 5, il adauga

# def nr_set_v2(nr, set):
#     if nr not in set:
#         set.add(nr)
#         print(f'Am adaugat numar nou in set: {set}')
#         return True
#     else:
#         print('Nu am adaugat numarul in set. Acesta exista deja.')
#         return False
# nr_set_v2(5,{1, 2, 3, 4}) #  pt 2, nu il adauga si pt 5, il adauga

# c. Optionale (may need google)
#
# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna
#
# calendar = {
#     'January' : 31,
#     'February' : 28,
#     'March' : 31,
#     'April' : 30,
#     'May' : 31,
#     'June' : 30,
#     'July' : 31,
#     'August' : 31,
#     'September' : 30,
#     'October' : 31,
#     'November' : 30,
#     'Dcember' : 31
# }
# # ----------------------------------
# def days(month):
#     return calendar.get(month)
# print(days('January'))
# # ----------------------------------
# def days(month):
#     if month in calendar:
#         return calendar.get(month)
# print(days('February'))


# 12. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
#
# def calculator(nr1, nr2):
#     suma = nr1 + nr2
#     diferenta = nr1 - nr2
#     inmultirea = nr1 * nr2
#     impartirea = nr1 / nr2
#     return suma, diferenta, inmultirea, impartirea
# suma, diferenta, inmultirea, impartirea = calculator(5,2)
# print(f'Suma: {suma}')
# print(f'Diferenta: {diferenta}')
# print(f'Inmultirea: {inmultirea}')
# print(f'Impartirea: {impartirea}')

# 13. NOT DONE YET!!!
# Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare litera
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
# list = [1, 3, 1, 5, 9, 7, 7, 5, 5]
# def letter_counter(list):
#     for i in list:
#         list.count[i]
#         counter +=1

# 14. Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele
# def max(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
# print(max(9,5 , 8))

# 15. NOT DONE YET!!!
# Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)
# a = 6
# def suma(list):
#     for
#
#     return
# BONUS:
#
# 16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
# ‘Numele este de baiat’ sau ‘Numele este de fata’
#
# exceptii_fete = ['Carmen', 'Iris', 'Damaris']
# exceptii_baieti = ['Mihnea', 'Mircea', 'Horia']
#
# def gen(nume_input):
#     if (nume_input[len(nume_input)-1] == 'a' or nume_input in exceptii_fete) and nume_input not in exceptii_baieti:
#         print('Este fata.')
#         return 'Este fata.'
#     else:
#         print('Este baiat.')
#         return 'Este baiat.'
# (gen('Mihnea'))

# 17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune
#
# Ex:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# # Raspuns: {2, 3}
#
# def liste(lista1, lista2):
#     lista3 = []
#     for i in lista1:
#         for j in lista2:
#             if i == j and i not in lista3:
#                 lista3.append(lista1[i])
#     return lista3
# print(liste(list1, list2))

# 18. Functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
#
# def reducere(x):
#     pret_produs = 100
#     if x <= 100:
#         pret_produs = pret_produs - pret_produs * x / 100
#         return int(pret_produs)
# print(f'Pretul duoa reducere este {reducere(10)} lei')

# 19. Functie care sa afiseze data si ora curenta
# from datetime import date
#
# def current_date():
#     current_date = date.today()
#     return current_date
# print(f'Data curenta este: {current_date()}')

# 20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau
# pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
from datetime import date

# def days_left():
#     my_birthday = date(year = 2022, month = 12, day = 5)
#     left = (my_birthday -date.today()).days
#     return left
# print(f'Pana la ziua mea mai sunt {days_left()} zile')