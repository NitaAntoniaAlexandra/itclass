#b. Usor spre Mediu (obligatoriu)
# #Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
# #Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if
# #X poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte.
## X este un int
#
# #1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
# # Un if else permite rularea codului in functie de conditiile necesare: if (conditia 1) este indeplinita,
# #se ruleaza blocuri de cod; daca acea conditie 1 nu este indeplinita (else) se ignora blocurile de cod de la if
# #si se ruleaza direct blocurile de cod de la else.


#2.  #Verifica si afiseaza daca x este numar natural sau nu
x =int(input('numarul ales este : '))
if x >= 0 :
   print('Numarul ales este numar natural')
else:
  print('Numarul ales nu este numar natural')


#3. # Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
x =int(input('numarul ales este : '))
if x == 0 :
    print('numarul ales este neutru')
elif x > 0:
    print('numarul ales este pozitiv')
else:
  print('numarul ales este negativ')

#4 Verifica si afiseaza daca x este intre -2 si 13
x =int(input('numarul ales este : '))
if -2 <= x and x <=13 :
    print('numarul ales apartine intervalului -2: 13 ')
else:
   print('numarul ales nu apartine intervalului -2: 13 ')

# 5. # Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
x =int(input('x este : '))
y =int(input('y este : '))
print(x-y)
if x - y < 5:
    print("diferenta dintre x si y este mai mica decat 5")
else:
  print("diferenta dintre x si y este mai mare decat 5")
# daca x este : 4, y este : 2566, diferenta lor x-y=-2562. este un numar negativ, care este mai mic decat 5.

#6.Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

x = int(input('numarul ales este : '))
if not(5 <= x and x <= 27) :#
    print('numarul ales nu apartine intervalului 5: 27 ')
else:
    print('numarul ales  apartine intervalului 5: 27 ')

#7.# x si y (int) # Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
x =int(input('x este : '))
y =int(input('y este : '))
if x!= y:
    print(' x si y sunt diferite')
    if x > y:
        print(' x este mai mare decat y')
    else:
        print(' y este mai mare decat x')
else:
    print(x==y)

# # 8.X, y, z - laturile unui triunghi. Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
x =int(input('x este : '))
y =int(input('y este : '))
z =int(input('z este : '))
if x != y and x == z or x == y and x != z:#triunghiul isoscel are 2 laturi egale
    print('triunghiul este isoscel')
elif x == y == z:#triunghiul echilateral are 3 laturi egale
    print('triunghiul este echilateral ')
else:
    print('triunghi este oarecare')#triunghiul oarecare are 3 laturi diferite



## 9.# Citeste o litera de la tastatura. Verifica si afiseaza daca este vocala sau nu
# #vocale 'a''e''i''o''u''ă''î''â''A''E''I''O''U''Ă''Î''Â' # este o modalitate sa excludem dintr-o lista anumite caractere? de ex sa facem if "litera" != "caracterele din vocale", print " nu este vocala"
litera = input('alege o litera')
if litera =='a'or litera =='e'or litera =='i'or litera =='o'or litera =='u' or litera =='î' or litera =='â' or litera=='Î' or litera=='Â' or  litera=='ă' or litera=='A' or litera=='E' or litera=='I'or litera=='U'or litera=='O':
     print('litera aleasa este o vocala')
else:
     print('litera aleasa nu este o vocala')


# 10.
# Transforma si printeaza notele din sistem romanesc in sistem american dupa cum urmeaza
## Peste 9 => A
# #Peste 8 => B
# #Peste 7 => C
# #Peste 6 => D
# #Peste 4 => E
# #4 sau sub => F
nota = int(input('nota este : '))
if 1 <= nota and nota<= 10:
    print('Mom I got a grade today')
    if 9 <= nota and nota<= 10:
        print('My grade is A')
    elif nota == 8:
        print('My grade is B')
    elif nota == 7:
        print('My grade is C')
    elif nota == 6:
        print('My grade is D')
    elif 4 < nota and nota< 6:
        print('My grade is E')
    elif nota>= 1 and nota<= 4:
        print('My grade is F')
else:
    print('Mom, no grade today')


# #C. Optionale (may need google)
#
# 11.Verifica daca x are minim 4 cifre(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = int(input ('numarul este : '))
if x >=+1000: # cel mai mic nr de 4 cifre
    print('numarul are minim 4 cifre')
#elif x<= -1000: # am facut si la negative
    print('numarul are mai mult de 4 cifre ')
else:
    print('numarul are mai putin de 4 cifre')


# #12.# Verifica daca x are exact 6 cifre

x = int(input ('numarul este : '))
if x >= 100000 and x <=999999: # daca x este in intervalul format dintre cel mai mic si cel mai mare nr de 6 cifre
    print('numarul are exact 6 cifre')
# elif x>=-999999 and x <= -100000: # am facut si la nr negative
    print('numarul are exact 6 cifre')
else:
    print('numarul nu are exact 6 cifre')

#13. Verifica daca x este numar par sau impar
x = int(input ('numarul este : '))
if x%2 == 1: # restul impartirii unor numere este 1 la numerele impare
    print('numarul este impar')
else:
    print('numarul este par')



# #14. x, y, z (int). # Afiseaza care este cel mai mare dintre ele?
x =int(input('x este : '))
y =int(input('y este : '))
z =int(input('z este : '))
if x==y and x==z and y==z:
    print(f'numerele sunt egale')
elif x>y and x>z:
    print( ' x este cel mai mare nr')
elif z>x and z>y:
    print('z este cel mai mare nr ')
elif y>x and y>z:
    print(' y este cel mai mare nr')
elif x==y and x==z and y==z:
    print(f'numerele sunt egale')
elif x == y and x>z:
    print(f'numerele sunt diferite, x si y sunt mai mari decat z')
else:
    print(f'numerele sunt diferite, x si z sunt mai mari decat y')



# #15. X, y, z - reprezinta unghiurile unui triunghi. Verifica si afiseaza daca triunghiul este valid sau nu
## suma unghiurilor sa fie 180, dar mai trebuie o conditie 0+0+180 nu e triunghi desi are suma 180
x =int(input('x este : '))
y =int(input('y este : '))
z =int(input('z este : '))
if x+y+z==180 and x>0 and y>0 and z>0 and x!=180 and y!=180 and z!=180:
    print(' Triunghiul este valid')
else:
    print('Triunghiul nu este valid')

#
##Bonus la cerere:
##17.Verificare imbarcare persoane : Tineti urmatoarele date
## Varsta
# #Insotit de mama
# #Insotit de tata
# #Pasaport
# #Act permisiune mama
# #Act permisiune tata

# #Conditii de imbarcare
# #Daca pers are varsta peste 18 ani si are pasaport
# #Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# #Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte
# Ex: # Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
# Etc
# Aici vreau sa testati codul cu toate variantele posibile. Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results
v = int(input('introdu varsta'))

pasaport = input('aveti pasaport? ')
# cu_mama = input('calatoriti cu mama? ')
# cu_tata = input('calatoriti cu tata? ')
# act_mama = input('aveti permisiune in scris de la mama?')
# act_tata = input('aveti permisiune in scris de la tata?')

if 0<v<18 and pasaport== 'da' :#minor cu pasaport ok dar mai trebuie si alte conditii
    print(' va rog raspundeti la urmatoarele intrebari')
    cu_mama = input('calatoriti cu mama? ')
    cu_tata = input('calatoriti cu tata? ')
    act_mama = input('aveti permisiune in scris de la mama?')
    act_tata = input('aveti permisiune in scris de la tata?')
    if cu_tata == 'da' and cu_mama=='da': # minor dar cu ambii parinti ok, else not ok
        print('Imbarcare cu succes')
    elif cu_tata =='da'and cu_mama == 'nu' and act_mama=='da': # minor,doar cu tata si act mama ok, else not ok
        print('Imbarcare cu succes')
    elif cu_tata =='nu' and cu_mama == 'da' and act_tata=='da':# minor,doar cu mama si act tata ok, else not ok
        print('Imbarcare cu succes')
    else:
        print('Imbarcare esuata')
elif v>=18 and pasaport =='da':
    print('Imbarcare cu succes')
else:
    print('Imbarcare Esuata')




##18. Joc ghicit zarul Cauta pe net si vezi cum se genereaza un numar random. Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll
# Luati un nr ghicit de la utilizator
# Verificati si afisati daca utilizatorul a ghicit
# 3 optiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# Ai ghicit. Felicitari? Ai ales x si zarul a fost y

# Luati un nr ghicit de la utilizator
import random
dice_roll = random.randint(1,6)

x = int(input('Alegeti un numar dat cu zarul, de la 1 la 6: '))

# Verificati si afisati daca utilizatorul a ghicit 3 optiuni
#Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
if x < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x}, dar a fost {dice_roll}.')

#Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
elif x > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x}, dar a fost {dice_roll}.')

#Ai ghicit. Felicitari? Ai ales x si zarul a fost y
else:
    print(f'Ai ghicit. Felicitari? Ai ales {x} si zarul a fost {dice_roll}.')