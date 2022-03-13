# # # Functii
# # # simple
# # def say_hi():
# #     print('Hi!')
# #
# # say_hi()
# # x=say_hi()
# # print(x)
# # #  cu parametri
# # def print_hi(user):#user este parametrul, pot fi mai multi, se separa prin virgula
# #     print(f'Hi {user}!')
# #
# # print_hi('ale')# ale, miau sunt argumente
# # print_hi('miau')
# #
# # # #return- reda output care se poate salva in variabila
# # def is_natural (numar):
# #     if numar >= 0:
# #         return 'numarul este natural'# ultima chestie din functie
# #     else:
# #         return 'numarul nu este natural'
# # raspuns = is_natural(3)
# # print(raspuns)
#
# #input 5 nr, output - ne dorim un set
# def make_set(n1,n2,n3):
#     r = set()
#     r.add(n1)
#     r.add(n2)
#     r.add(n3)
#     return r
#
#
# print(make_set(1,2,3))
# # print(make_set(1,2,2))
# # #cand apelez functia trebuie sa vizualizez rezultatul
# #
# #
# # #functie cu return dar fara parametri
# # def pi_value():
# #     return 3.14
# #
# # x = pi_value()+4
# # print(x)
# # from Cursuri.functii_helpers import *
# # print(suma(4,6))
# # from Cursuri.functii_helpers import *# importa toate functiile din functii_helpers
#
#
#
# #calculator de impozit in functie de cc
# cc = int(input('Alege centimetri cubi  '))
# impozit = None
# def calcul_impozit(cc_input, hibrid_input):
#     if hibrid_input == True:
#         return 10
#     else:
#         if cc_input < 1000:
#             return 70
#         elif cc_input <2000:
#             return 160
#         else:
#             return 900
#
#
#
# #apelam functia
# impozit = calcul_impozit(cc, False)
# print(impozit)#cc 49= 70
# impozit= calcul_impozit(2400, False)
# print(impozit)# =900
# impozit = calcul_impozit(2400, True)
# print(impozit)#10

# de benzina ramasa + daca scadem sun 15%, afisam un warning
#return un procent 10
REZERVOR = 50
cantitate_benzina = float(input('Introdu cantitatea de benzina: '))
def consum_benzina(cantitate_benzina, procent):
    if cantitate_benzina == 0:
        return ('Caut-o sticla')
    elif cantitate_benzina < 7.5:
        return ('Atentie, cauta o benzinarie')
    else:
        return ('Vrummm, Vruummm')


# nume_dat = input(' spune un nume')
# def nume