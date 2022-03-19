#a. Recomandat (usor)
#1. Revizualizeaza intalnirea 6 si ia notite in caz ca ti-a scapat ceva

#b. Obligatorii (mediu)
#Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei

#1. Clasa Cerc
#Atribute: raza, culoare
#Constructor pt ambele atribute

#Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

# class Cerc:
#     #atribute
#     r = None
#     culoare =None
#     PI = 3.14
#
#     #constructor
#     def __init__(self, r, culoare):
#         self.r = r
#         self.culoare = culoare
#
#
#     #metode
#
#     def descriere(self):
#         print(f'Cercul are culoarea {self.culoare} si raza {self.r}')
#
#     def aria(self):
#         if self.r > 0:
#             aria = float(self.r*self.r*self.PI)
#             # return (f'aria cercului este {aria}')# aria() - va RETURNA aria???" not within a nested class definition."
#             print(f'Aria cercului este {aria}')
#         else:
#             print(f'Raza trebuie sa fie un nr pozitiv')
#
#     def diametru(self):
#         if self.r > 0:
#             diametru = float(self.r+self.r)
#             print(f'Diamentrul cercului este {diametru} ')
#         else:
#             print(f'Raza trebuie sa fie un nr pozitiv')
#     def circumferinta(self):
#         if self.r > 0:
#             circumferinta = float(self.PI*self.r*2)
#             print(f'Circumferinta cercului este {circumferinta} ')
#         else:
#             print(f'Raza trebuie sa fie un nr pozitiv')
#
#
# #initializare obiecte
# cerc1 = Cerc(3,'galben')
# cerc2 = Cerc(-9,'maro')
# cerc3 = Cerc(4.5, 'negru')
#
# cerc1.descriere()
# cerc2.descriere()
# cerc3.descriere()
#
# cerc1.aria()
# cerc2.aria()
# cerc3.aria()
#
# cerc1.diametru()
# cerc2.diametru()
# cerc3.diametru()
#
# cerc1.circumferinta()
# cerc2.circumferinta()
# cerc3.circumferinta()




# 2.
# Clasa Dreptunghi
## Atribute: lungime, latime, culoare
## Constructor pt toate atributele
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
#
#
# class Dreptunghi:
#
#     lungime = None
#     latime = None
#     culoare = None
#
#
#     def __init__(self, lungime, latime, culoare):
#         self.latime = latime
#         self.lungime = lungime
#         self.culoare = culoare
#
#
#     def descrie(self):
#         print(f'Dreptunghiul cu lungimea {self.lungime} si latimea {self.latime} are culoarea {self.culoare}.')
#
#     def aria(self):
#         if self.latime >0 and self.lungime > 0:
#             aria = float(self.lungime*self.latime)
#             print(f'Aria dreptunghiului este {aria}.')
#         else:
#             print(f'Mai masoara dreptunghiul!')
#
#     def perimetru(self):
#         if self.latime >0 and self.lungime > 0:
#             perimetrul = float(self.lungime*2+ self.latime*2)
#             print(f'Perimetrul dreptunghiului este {perimetrul}.')
#         else:
#             print(f'Mai masoara dreptunghiul!')
#
#     def paint(self, culoare):
#         self.culoare = culoare
#
#
# drpt1 = Dreptunghi(2, 6, 'maro')
# drpt2 = Dreptunghi(-8, 10,'alb')
# drpt3 = Dreptunghi(7,3, 'rosu')
#
# drpt1.descrie()
# drpt2.descrie()
# drpt3.descrie()
#
# drpt1.aria()
# drpt2.aria()
# drpt3.aria()
#
# drpt1.perimetru()
# drpt2.perimetru()
# drpt3.perimetru()
#
# drpt1.paint('roz')
# drpt2.paint('verde')
# drpt3.paint('orange')
# drpt1.descrie()
# drpt2.descrie()
# drpt3.descrie()
#
#
#
#
# # 3.
# # Clasa Angajat
# #
# # Atribute: nume, prenume, salariu
# #
# # Constructor pt toate atributele
# #
# # Metode:
# # descrie()
# # nume_complet()
# # salariu_lunar()
# # salariu_anual()
# # marire_salariu(procent)
# #
# class Angajat:
#     nume = None
#     prenume = None
#     salariu = 0
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(f'Angjatul {self.nume} {self.prenume} are salariul {self.salariu} Ron.')
#
#     def nume_complet(self):
#         print(f'Numele complet al angajatului este {self.nume} {self.prenume}')
#
#     def salariu_lunar(self):
#         if self.salariu >0:
#             print(f'Salariul lunar al angajatului {self.nume} este {self.salariu} Ron.')
#         else:
#             print(f'Verificati daca angajatul este platit')
#
#     def salariu_anual(self):
#         if self.salariu > 0:
#             salariul_anual = self.salariu*12
#             print(f'Salariul anual al angajatului {self.nume} este {salariul_anual} Ron.')
#         else:
#             print(f'Verificati daca angajatul este platit')
#
#     def marire_salariu(self,marire):
#         if self.salariu > 0:
#             self.marire =marire
#             self.salariu =self.salariu/100*self.marire+self.salariu
#             print(f'Salariul marit al angajatului {self.nume} este {self. salariu} Ron.')
#             print(f'Marirea angajatului {self.nume} consta in {self.marire} procente ')
#         else:
#             print(f'Verificati daca angajatul este platit')
#
#
# angajat1 = Angajat('Marcu', 'Aurel', 2500)
# angajat2 = Angajat('Mihaiu', 'Ioana', -1520)
# angajat3 = Angajat( 'Neculcea', 'Mirabela', 3450)
#
# angajat1.descrie()
# angajat2.descrie()
# angajat3.descrie()
#
# angajat1.nume_complet()
#
# angajat1.salariu_lunar()
# angajat2.salariu_lunar()
# angajat3.salariu_lunar()
#
# angajat1.salariu_anual()
# angajat2.salariu_anual()
# angajat3.salariu_anual()
#
# angajat1.marire_salariu(10)
# angajat2.marire_salariu(25)
# angajat3.marire_salariu(2)



# 4.
# Clasa Factura
#
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
#
# Constructor: toate atributele, fara serie
#
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
#
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 49000
#
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
#
from datetime import date

class Factura:
    Seria = 'A'
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc


    def schimba_cantitatea(self, cantitate):
        cantitate = float(input('Alege o cantitate:  '))
        self.cantitate = cantitate
        print(f'Cantitatea noua este {self.cantitate}')
    def schimba_pretul(self, pret_buc):
        pret_buc = float(input('Alege un pret : '))
        self.pret_buc = pret_buc
        print(f'Pretul nou este {self.pret_buc}')
    def schimba_nume_produs(self, nume_produs):
        nume_produs = input('Noul produs ales este: ')
        self.nume_produs = nume_produs
        print(f'Noul produs este {self.nume_produs}')
    def genereaza_factura(self):
        print(f'Factura seria {self.Seria}, numar {self.numar}')
        today = date.today()
        print(f'Data: {today}')
        print('Produs   | cantitate   | pret bucata   | Total  ')
        Total=self.cantitate*self.pret_buc
        print(f'{self.nume_produs}  |      {self.cantitate}      |    {self.pret_buc}       |    {Total}   ')
        #
fact1 = Factura(1, 'masina' , 1, 17000)
fact1.genereaza_factura()
fact2=Factura(2,'remorca',2, 1900)
fact2.genereaza_factura()
#


# 5.# Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)
class Cont:
    iban: None
    titular_cont = None
    sold = None

    def __init__(self,iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold}')
    def debitare_cont(self, suma):
        sold = self.sold - suma
        print(f'Cu ce suma se debiteaza contul? {suma}')
        print(f'Soldul actual dupa debitare este {sold}')
    def creditare_cont(self, suma):
        sold = self.sold+suma
        print(f'Cu ce suma se crediteaza contul? {suma}')
        print(f'Soldul actual dupa creditare este {sold}')


cont1 = Cont(123124143,'ana', 1000)
cont1.creditare_cont(100)
cont1.debitare_cont(500)
# Cu ce suma se crediteaza contul?100
# Soldul actual dupa creditare este 1100 #imi crediteaza de la 1000 cum i-am cerut
# Cu ce suma se debiteaza contul? 500
# Soldul actual dupa debitare este 500 imi debiteaza de la 1000 din nou. inteleg ca ia self.sold dar ar trebui sa am legatura intre ele? ex creditez cu o suma si din soldul nou sa debitez alta valoare?

