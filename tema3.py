## 1.Declara o lista note_muzicale in care sa pui do re mi etc pana la do
## 1. Afiseaz-o
## 2. Inverseaza ordinea folosind slicing si suprascrie aceasta lista
## 3. Printeaza varianta actuala (inversata)
## 4. Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
## 5. Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
## Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
note_muzicale = [ 'do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale[ ::-1])# slice
gama= note_muzicale[ ::-1]# suprascriere
print(note_muzicale)
note_muzicale.reverse()#inverseaza caracterele in functie de index, de la ultimul la primul
print(note_muzicale)
#2. De cate ori apare ‘do’?
print(note_muzicale.count('do'))

#3.Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]. Gasiti 2 variante sa le uniti intr-o singura lista.
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista3 = lista1+lista2# varianta 1
#lista3 = lista1.__add__(lista2)# varianta 2
print(lista3)


#4.Sortati si afisati lista generata la ex anterior. Stergeti numarul 0 folosind o functie, Afisati iar lista
lista3.sort()
print(lista3)
lista3.remove(0)
print(lista3)
#5. Folosind un if verificati lista generata la ex3 si afisati * Lista este goala* Lista nu este goala
if len(lista3) == 0:
    print('lista este goala')
else:
    print('lista nu este goala')
#6. Folositi o functie care sa stearga lista de la ex3
lista3.clear()
print(lista3)
#7. Copy paste la ex 5. Verificati inca o data.Acum ar trebui sa se afiseze ca lista e goala
if len(lista3) == 0:
    print('lista este goala')
else:
    print('lista nu este goala')



# 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}. Folositi o functie ca sa afisati Elevii (cheile)
dict1  = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())


#9. Printati cei 3 elevi si notele lor. Ex: ‘Ana a luat nota {x}’. Doar nota o veti lua folosindu-va de cheie

print('Ana a luat nota '+ str(dict1['Ana']))
print('Gigel a luat nota '+ str(dict1['Gigel']))
print('Dorel a luat nota '+ str(dict1['Dorel']))


#10. Dorel a facut contestatie si a primit 6. Modificati nota lui Dorel in 6.Printati nota dupa modificare

dict1['Dorel'] ='6'
print(dict1)
print('Dorel a luat nota '+ str(dict1['Dorel']))

#11.Gigel se transfera din clasa. Cautati o functie care sa il stearga. Vine un coleg nou. Adaugati Ionica, cu nota 9.
#Printati noii elevi
dict1.pop('Gigel')
print(dict1)
dict1['Ionica']= 9
print(dict1)


#12.Set zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'} weekend = {'sambata', 'duminica'}
# Adaugati in zilele_sapt ‘luni’. Afisati zile_sapt
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
zile_sapt.add('luni') # nu exista dubluri
print(zile_sapt)


#13. Folositi un if si verificati daca * Weekend este un subset al zilelor din sapt
#* Weekend nu este un subset al zilelor din sapt
weekend = {'sambata', 'duminica'}
if weekend.issubset(zile_sapt):
   print('Weekend este un subset al zilelor din sapt ')
else:
   print('Weekend nu este un subset al zilelor din sapt')


#14.  Afisati diferentele dintre aceste 2 seturi
print(zile_sapt.difference( weekend))


# 15.Afisati intersectia elementelor din aceste 2 seturi
print(zile_sapt.intersection( weekend))


