# ##16.Verificare imbarcare persoane : Tineti urmatoarele date
# ## Varsta
# # #Insotit de mama
# # #Insotit de tata
# # #Pasaport
# # #Act permisiune mama
# # #Act permisiune tata
#
# # #Conditii de imbarcare
# # #Daca pers are varsta peste 18 ani si are pasaport
# # #Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# # #Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte
# # Ex: # Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# # Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
# # Etc
# # Aici vreau sa testati codul cu toate variantele posibile. Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results
#
#
# v = int(input('introdu varsta'))
# pasaport = input('aveti pasaport? ')
#
# if v<17.99 and pasaport== 'da' :#minor cu pasaport ok dar mai trebuie si alte conditii
#     print(' va rog raspundeti la urmatoarele intrebari')
#     cu_mama = input('calatoriti cu mama? ')
#     cu_tata = input('calatoriti cu tata? ')
#     act_mama = input('aveti permisiune in scris de la mama?')
#     act_tata = input('aveti permisiune in scris de la tata?')
#     if cu_tata == 'da' and cu_mama=='da': # minor dar cu ambii parinti ok, else not ok
#         print('Imbarcare cu succes')
#     elif cu_tata =='da'and cu_mama == 'nu' and act_mama=='da': # minor,doar cu tata si act mama ok, else not ok
#         print('Imbarcare cu succes')
#     elif cu_tata =='nu' and cu_mama == 'da' and act_tata=='da':# minor,doar cu mama si act tata ok, else not ok
#         print('Imbarcare cu succes')
#     else:
#         print('Imbarcare esuata')
# elif 18<=v and pasaport =='da':
#     print('Imbarcare cu succes')
# else:
#     print('Imbarcare Esuata') # varsta scrisa gresit
# actual results
# introdu varsta50
# aveti pasaport? da
# Imbarcare cu succes

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