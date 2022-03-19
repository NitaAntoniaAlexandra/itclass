# Pentru toate exercitiile
# Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
# Daca functia are return, printati raspunsul

#1. Functie care sa calculeze si sa returneze suma a 2 numere
a = int(input(' alege primul nr:  '))# parametru alatoriu
b = int(input(' alege al doliea nr:  '))
def suma(a, b):
    return a+b
suma(a, b)
print(suma(a,b))

# a = 4# parametru dat, specificand valorile pt fiecare
# b = 6
# suma(a, b)
# print(suma(a,b))
#
# suma(5, 9)# parametru nedefinit, dat direct
# print(suma(5,9))


# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
x = int(input(' alege un numar:  '))
def par_impar(x):
    if x%2==0:
        return  True
    else:
        return False

par_impar(x)# parametru aleatoriu
print(par_impar(x))
#
# par_impar(6)# parametru dat
# print(par_impar(6))
# par_impar(99)# parametru dat
# print(par_impar(99))

# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)
x = input('Numele tau este :  ' )
y = input('Prenumele tau este: ')
z = input('Numele tau mijlociu este: ')

def len_nume_complet(x, y, z):
    return len(x)+len(y)+len(z)

len_nume_complet(x,y,z)
print(f'Lungimea numelui complet este: ', len_nume_complet(x,y,z))

# x = 'a'
# y = 's'
# z = 'd'
# len_nume_complet(x,y,z)
# print('Lungimea numelui complet este: ', len_nume_complet(x,y,z)) #3 caractere
#
# len_nume_complet('Nita', 'Astrid', 'Stefania')
# print('Lungimea numelui complet este: ', len_nume_complet('Nita', 'Astrid', 'Stefania')) #18 caractere


# # 4. Functie care returneaza aria dreptunghiului
lungime = int(input('Lungimea dreptunghiului este: '))
latime = int(input('Latimea dreptunghiului este: '))
def ariaD (lungime,latime):
    if lungime >0 and latime> 0:
        return lungime*latime
    else:
        return ' Ai ales valori gresite, dimensioneaza din nou'

ariaD(lungime, latime)
print(ariaD(lungime, latime))

# print(ariaD(8, 8))#64



# 5.Functie care returneaza aria cercului
pi = 3.14
r = int(input(' Raza cercului este : '))
def aria_cerc(r):
    if r >0:
        return pi*r*r
    else:
        return 'Ai ales valori gresite, dimensioneaza din nou'

aria_cerc(r)#random
print(aria_cerc(r))
# aria_cerc(4)#definit
# print(aria_cerc(4))#50,24



#6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu
str = input(' Scrie un string: ')
x= input(' Selecteaza un caracter: ')
def x_prezent(x,str):
    if x in str:
        return True
    else:
        return False
x_prezent(x,str)
print(x_prezent(x,str))
# Scrie un string: abracadabra
#  Selecteaza un caracter: a
# True
# Scrie un string: abracadabra
#  Selecteaza un caracter: s
# False

#7. Functie fara return, primeste un string si printeaza pe ecran:
# -	Nr de caractere lower case este x
# -	Nr de caractere upper case exte y
string= input(' Scrie un string: ')
def nr_upper_lower(string):
    count1low = 0
    count2up = 0
    for i in string:
        if (i.islower()):
            count1low = count1low + 1
        elif (i.isupper()):
            count2up = count2up + 1
        else:
            print(' Stringul ales are si alte caractere in afara de litere')
    print(f' Stringul are {count1low} minuscule.' )
    print(f' Stringul are {count2up} majuscule.' )
nr_upper_lower(string)
# Scrie un string: annnaaaaAAAAAAAAAAA
#  Stringul are 8 minuscule.
#  Stringul are 11 majuscule.

# Scrie un string: 3ianuarie1900toamna
#  Stringul ales are si alte caractere in afara de litere#1
#  Stringul ales are si alte caractere in afara de litere#2
#  Stringul ales are si alte caractere in afara de litere#3
#  Stringul ales are si alte caractere in afara de litere#4
#  Stringul ales are si alte caractere in afara de litere#5
#  Stringul are 14 minuscule.
#  Stringul are 0 majuscule.

#  Scrie un string: Stai jos!Ai nota 2!
#  Stringul ales are si alte caractere in afara de litere
#  Stringul ales are si alte caractere in afara de litere
#  Stringul ales are si alte caractere in afara de litere
#  Stringul ales are si alte caractere in afara de litere
#  Stringul ales are si alte caractere in afara de litere
#  Stringul ales are si alte caractere in afara de litere
#  Stringul are 11 minuscule.
#  Stringul are 2 majuscule.
# ce interesant e ca imi arata si nr de alte caractere -spatiu, cifre, simboluri :)


# # 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
lista = [2,4,894,-481,-48,-87,+89,0,55,1]
lista_pozitive = []

def nr_poz(numere):
    for numar in numere:
        if numar > 0:
            lista_pozitive.append(numar)
    return(f'Lista nr pozitive este {lista_pozitive}')

print(nr_poz(lista))#Lista nr pozitive este [2, 4, 894, 89, 55, 1]

# 9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
# -	Primul numar x este mai mare decat al doilea nr y
# -	Al doilea nr y este mai mare decat primul nr x
# # -	Numerele sunt egale.
x = int(input('Primul nr este: '))
y = int(input('Al doilea nr este: '))
def functie_aleatorie(x, y):
    if x > y:
        print(f' Primul numar, {x},  este mai mare decat al doilea, {y}.')
    elif x< y:
        print(f' Al doilea nr, {y}, este mai mare decat primul nr, {x}.')
    else:
        print(f'Numerele sunt egale ')

functie_aleatorie(x,y)
print(functie_aleatorie(x,y))
# Primul nr este: 2
# Al doilea nr este: 2
# Numerele sunt egale
# Primul nr este: -410543
# Al doilea nr este: 21
#  Al doilea nr, 21, este mai mare decat primul nr, -410543.
# Primul nr este: 25410
# Al doilea nr este: 22405
#  Primul numar, 25410,  este mai mare decat al doilea, 22405.


# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
set = {1,2,3,4,5,6,7,8,9,100,-100, -99,+99}
def add(set, alt_nr):
    if alt_nr in set:
        print(f'nu am adaugat numarul {alt_nr} in set, exista deja')
        return False
    else:
        set.add(alt_nr)
        print(f'am adaugat numarul {alt_nr} in set')
        print(set)
        return True
add(set, 1)
# print(add(set, 111))
# print(add(set, 23))
# print(add(set, 23))
# nu am adaugat numarul 1 in set, exista deja
# am adaugat numarul 111 in set
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 99, 111, -100, -99}
# True
# am adaugat numarul 23 in set
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 99, 111, 23, -100, -99}
# True
# nu am adaugat numarul 23 in set, exista deja
# False


# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna
calendarul_vietii= {
    'ianuarie': '31',
    'februarie': '28',
    'martie':'31',
    'aprilie':'30',
    'mai':'31',
    'iunie':'30',
    'iulie':'31',
    'august': '31',
    'septembrie': '30',
    'octombrie':'31',
    'noiembrie':'30',
    'decembrie':'31'
}
def nr_zile(luna):
    return calendarul_vietii.get(luna)

print(nr_zile('mai'))#31

print(nr_zile('fdgh'))#None

# 12. Functie calculator care sa returneze 4 valori :Suma, diferenta, inmultirea, impartirea a 2 numere

#
a = int(input('alege primul nr: '))
b = int(input('alege al doilea nr: '))

def multiple_values(a,b):
    suma = a+b
    diferenta = a-b
    inmultire = a*b
    impartire = a/b
    return suma, diferenta, inmultire, impartire

# print(multiple_values(a,b))
# print(multiple_values(4,9))
#
suma, diferenta, inmultire, impartire = multiple_values(a,b)
print('suma este ',suma)
print('diferenta este ', diferenta)
print('inmultirea este ', inmultire)
print('impartirea este ', impartire)

# 13. Functie care primeste o lista de cifre (adica doar 0-9). Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5].
# Returneaza un DICT care ne spune de cate ori apare fiecare litera CIFRA???
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
lista_mea = [0,0,0,0,3,1,6,4,5,3,4,7,9,2,3,5,2]
dictionar = {0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
}
c0 = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
def recurenta(lista_mea):# nu am reusit sa o transform in functie, trebuie s-o mai editez
    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    c9 = 0
for numar in lista_mea:
    if numar == 0:
        c0=c0+1
        dictionar[0]=c0
    elif numar ==1:
        c1+=1
        dictionar[1]=c1
    elif numar == 2:
        c2+=1
        dictionar[2]=c2
    elif numar == 3:
        c3+=1
        dictionar[3]=c3
    elif numar == 4:
        c4+=1
        dictionar[4]=c4
    elif numar == 5:
        c5+=1
        dictionar[5]=c5
    elif numar == 6:
        c6+=1
        dictionar[6]=c6
    elif numar == 7:
        c7+=1
        dictionar[7]=c7
    elif numar == 8:
        c8+=1
        dictionar[8]=c8
    elif numar == 9:
        c9+=1
        dictionar[9]=c9
print(f'Cifra 0 apare de {c0}  ori')
print(f'Cifra 1 apare de {c1} ori')
print(f'Cifra 2 apare de {c2} ori')
print(f'Cifra 3 apare de {c3} ori')
print(f'Cifra 4 apare de {c4} ori')
print(f'Cifra 5 apare de {c5} ori')
print(f'Cifra 6 apare de {c6} ori')
print(f'Cifra 7 apare de {c7} ori')
print(f'Cifra 8 apare de {c8} ori')
print(f'Cifra 9 apare de {c9} ori')
print(dictionar)





#
# # 14. Functie care primeste 3 numere
# # Returneaza valoarea maxima dintre ele
a = int(input('Primul nr e: '))
b = int(input('Al doilea nr e : '))
c = int(input('Al treilea nr e : '))
def get_max(a,b,c):
    if a == b and a == c:
        return 'numerele sunt egale'
    elif a>b and a>c:
        return 'a este cel mai mare nr'
    elif b>a and b>c:
        return 'b este cel mai mare nr'
    elif c>a and c>b:
        return 'c este cel mai mare nr'
    elif a==b and a>c:
        return f'a si b sunt mai mari decat c'
    elif a==c and a>b:
        return f'a si c sunt mai mari decat b'
    else:
        return f'a si c sunt mai mari decat b'

get_max(a,b,c)
print(get_max(a,b,c))
# print(get_max(1,2,3))
# print(get_max(1,2,4))
# #

#
# 16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
# ‘Numele este de baiat’ sau ‘Numele este de fata’
exceptii_fete = ['Carmen', 'Iris', 'Damaris','Beatrice', 'Miriam','Zoe', 'Ingrid', 'Lili', 'Catrinel','Nico', 'Alice', 'Aglae', 'Lorelai']
exceptii_baieti = ['Mihnea', 'Mircea', 'Horia','Dima', 'Luca', 'Romica','Ghita', 'Gruia', 'Nichita' ],
nume = input('Numele ales este: ')
def fata_baiat(nume):
    if (nume[len(nume)-1] == 'a' or nume in exceptii_fete):
        return 'Numele este de fata .'
    elif (nume[len(nume)-1]) != 'a' or nume in exceptii_baieti:
        return 'Numele este de baiat'
print(fata_baiat(nume))

