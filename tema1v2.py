# 1.In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
# #Variabila este un spatiu din memorie care tine date.
# 2.# Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
# string, int, float, bool
# Valorile le alegeti voi dupa preferinte
a = 20
b = 20.10
c = 'python'
python_e_usor_de_invatat = False
# # 3. Utilizat functia type pentru a verifica ca ele au tipul de date asteptat
print(type(a))
print(type(b))
print(type(c))
print(type(python_e_usor_de_invatat))

# # 4.Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
# Verificati tipul acesteia
q = 20.8
print(round(q))
q = print(round(q))

# #5. folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
# (rezolvati nepotrivirile de tip prin ce modalitate doriti)
varsta = 32
varsta_copilului = 1.7
locuiesc_in  = 'Brasov'
d = 'python nu e usor de invatat'
print('Sunt Alexandra, am '+ str(varsta) + ' de ani, am o fetita de '+ str(varsta_copilului) + ' ani, stam in '+ str(locuiesc_in) + ' si cred ca '+ d)
bool(d)==True



# 6.# citeste de la tastatura numele
# citeste de la tastatura prenumele
# afiseaza 'Numele complet are x caractere'
#
nume =input('introdu numele')
prenume = input(('introdu prenumele'))
x= len(nume+prenume)
print('Numele complet are ' + str(len(nume+prenume)) + ' caractere')
print('Numele complet are ' + str(x) + ' caractere')

# 7.# # citeste de la tastatura lungimea
# #citeste de la tastatura latimea
# #afiseaza 'Aria dreptunghiului este x'
#
latimea = input('introdu latimea')
lungimea = input('introdu lungimea')
a = int(latimea)*int(lungimea)
print( 'Aria dreptunghiului este '+ str(a))


# # 8.# Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# cititi de la tastatura un int x,# afiseaza stringul fara ultimele x caractere
# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
my_string = 'Coral is either the stupidest animal or the smartest rock'
x = input('cate caractere elimini?: ')
print(len(my_string)-int(x))
print(my_string[0:len(my_string)-int(x)])



# 9.# acelasi string
# declara un string nou care sa fie format din primele 5 caractere + ultimele 5
# my_string = 'Coral is either the stupidest animal or the smartest rock'
my_string2 = print(my_string[0:5]+my_string[-5:])


# 10.# acelasi string
# afisati de cate ori apare cuvantul 'the'
my_string = 'Coral is either the stupidest animal or the smartest rock'
print(my_string.count('the'))

# 11. # acelasi string
# inlocuieste the cu THE peste tot
# printeaza rezultatul
my_string = 'Coral is either the stupidest animal or the smartest rock'
print(my_string.replace('the', 'THE'))

# 12. # acelasi string
# salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
# (hint: este o functie care te ajuta sa faci asta)
# folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest '
my_string = 'Coral is either the stupidest animal or the smartest rock'
aha = print(my_string.index('rock')) #ok
print(my_string.split('rock'))


# 13. citeste de la tastatura un string
# # verifica daca primul si ultimul caracter sunt la fel
# # se va folosi un assert
# # atentie: se doreste ca programul sa fie case insensitive
# # 'apA' e acceptat
sir = str.casefold(input('sirul meu este: '))
#print(sir[0])
#print(sir[-1])
assert sir[0] == sir[-1] #comparam daca primul caracter = ultimul

#14.# avand stringul '0123456789'
# afisati doar numerele pare
# acum afisati doar numerele impare
# (hint: folositi slicing, controlati din pas)
s = '0123456789'
print(s[0: :2])
print(s[1: :2])


# 15.# acelasi string de la 12
# folositi un assert ca sa verificati daca acest string contine doar numere
# hint: merge cu slicing? probabil ca nu... ce mai stim atunci legat de string?
# poate gasim o functie ajutatoare
my_string = 'Coral is either the stupidest animal or the smartest rock'
print(my_string.isalnum())
# print(my_string.isalpha())

# c. Optionale (may need google)
# 16.# citeste de la tastatura un string de dimensiune impara
# afiseaza caracterul din mijloc
ss = input('scrie un cuvant de dimensiune impara : ') # ok
print(f'Lungimea stringului ales este {len(ss)}') # aflu len ok
x= len(ss)
if x % 2 == 1:
    print('cuvantul are dimensiune impara')
    print(f'caracterul din mijloc are pozitia {int(x / 2)}')
    y = int(x / 2)
    print(f'Caracterul din mijloc este {ss[y]}')
else:
    print('cuvantul are dimensiune para')


# 17.# Folosind assert, verificati daca un string este palindrom
palindrom = input('introdu un cuvant')
assert (palindrom == palindrom[::-1])
print('Cuvantul ales este palindrom')


# 20.# citeste un user de la tastatura
# citeste o parola
# afiseaza: 'Parola pt user x este ***** si are x caractere'
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
# eg: parola abc => ***
# parola abcd => ****
user_name = input('username') # definim user name ok
password = input('password') # definim parola ok
hidden_pass= '*'* len(password)
print(len(hidden_pass)) # vrem sa printam lungimea paroleiok
print(hidden_pass)
# # #vrem sa inlocuim parola cu caractere asterix ok
print(password.replace(password, str(len(password)*'*')))

print('The password for user ' + str(user_name)  +' is ' + hidden_pass + ' is '+ str(len(hidden_pass))+ ' characters long')
# #