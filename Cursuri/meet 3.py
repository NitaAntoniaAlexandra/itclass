# # liste
# # accesarea unui element list. [nr index]
# #nume == 'Alex'
# nume_as_list = ['A', 'l', 'e', 'x']
# print(nume_as_list[0])
# # aflam len
# print(len(nume_as_list))
# # putem face slice
# print(nume_as_list[ 0:2])
# # eliminarea unui caracter
# nume_as_list.remove('l')# in functie de valoare
# nume_as_list.pop()# in functie de index, default ultimul si il putem salva ca si o variabila
# # suprascriere
# nume_as_list[0]=='a'
# print(nume_as_list)
# #
# # adaugare la index
# nume_as_list.insert(0, 'A')
# # adaugare la final
# nume_as_list.append('M')





#c. Optionale (may need google)
# 16. Ne imaginam o echipa de fotbal pt teren sintetic. 3 Schimbari maxime admise
# Declara o Lista cu 5 jucatori Schimbari_efectuate = va jucati voi cu valori diferite
#
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# * Efectuam schimbarea
# * Stergem jucatorul scos din lista
# * Adaugam jucatorul intrat
# * Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# * Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# * Afisati ‘mai aveti z schimbari’
# Testati codul cu diferite valori
#echipa1 = ['Helmuth Duckadam', 'Ștefan Iovan (c)', 'Miodrag Belodedici', 'Adrian Bumbescu', 'Ilie Bărbulescu', 'Gavril Balint', 'Lucian Bălan', 'Ladislau Bölöni', 'Mihail Majearu', 'Marius Lăcătuș', 'Victor Pițurcă', 'Anghel Iordănescu', 'Marin Radu', 'Emerich Jenei']
#schimbari=['Lucian Bălan', 'Marius Lăcătuș', 'Anghel Iordănescu', 'Marin Radu', 'Emerich Jenei']
#if 'Lucian Bălan'
echipa = {'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8', 'j9', 'j10', 'j11'}
rezerve = {'j12', 'j13', 'j14', 'j15', 'j16'}
# vreau sa schimb j1 cu j12, j2 cu j13 si j3 cu j14
if not rezerve.issubset(echipa):
   print('puteti alege urmatorii jucatori '+ str(rezerve))


# echipa.remove('j1')
# #echipa.append('j12')
# print(echipa)
# echipa.remove('j2')
# #echipa.append('j13')
# print(echipa)
# echipa.remove('j3')
# #echipa.append('j14')
# print(len(echipa))
# nr_jucatori= len(echipa)
# if nr_jucatori == '11':
#    print('mai aveti 3 schimbari la dispozitie')
#    if nr_jucatori == '10':
#       print('mai aveti 2 schimbari la dispozitie')
#    elif nr_jucatori == '9':
#       print('mai aveti 1 schimbare la dispozitie')
# else:
#    print('nu mai aveti schimbari la dispozitie')



# lista_jucatori = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5']
# print(lista_jucatori)
# jucator_schimbat = 'jucator1'
# schimbari = [0, 1, 2, 3]
# print(schimbari)
# schimbari_efectuate = 3
# schimbari_maxime = 3
# schimbari_ramase = schimbari_maxime - schimbari_efectuate
# print(schimbari_ramase)
# if jucator_schimbat in lista_jucatori and schimbari_efectuate in schimbari:
#    print('jucatorul poate fi schimbat')
#    lista_jucatori.remove(jucator_schimbat)
#    print(lista_jucatori)
#    jucator_nou = 'jucator6'
#    lista_jucatori.append(jucator_nou)
#    print(lista_jucatori)
#    print(f'A intrat {jucator_nou} a iesit {jucator_schimbat}, mai aveti', schimbari_ramase, 'schimbari')
# else:
#    print('jucatorul nu e pe teren')
#    if schimbari_ramase <= 0 or schimbari_ramase > 3:
#        print('nu mai aveti dreptul la alte schimbari')