# # operatori de atribuire
# x = 3
# x+=7
# print(x) # suprascrie
#
# # la fel ca si x = x + 10
# #nu e acelasi lucru ca si x=+7!!!!
# #op aritmetici
# #op de comparare
# # print(3 == 3)#true
# # print(3 != 3) #false
# # print(3<3) #false
# # print(3<=3)#true
# # #operatori logici
# #and, or, not
# print((3 >0 and 5>0))
# print(-3>0 or 5>0)
# #true or false => true
# #false or false => false
# #true or true=> true
# print(not(-3>0 or -5 > 0))#not - inverseaza raspunsul



#if, if else, elif
nota_de_trecere_examen = 4.5 # constanta, nu se schimba
nota_de_trecere_purtare = 7
if 7>nota_de_trecere_examen and 9>= nota_de_trecere_purtare :
    print(('am trecut clasa'))
#if else
if 3>nota_de_trecere_examen and 9>= nota_de_trecere_purtare :
    print(('am trecut clasa'))
else:#nu are conditie
    print('nu am trecut clasa')

# if else if else....
#ordinea este if, elif oricate, apoi else