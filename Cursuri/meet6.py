# class Car:
#     make = 'Dacia' # fields sau atribute
#     model = None
#     year = 2022
#     color = None
#
#
#
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color+ 'uriu'
#
#     #metode
#     def accelerate(self):
#         print('Vruuuum!')
#
#     def paint(self, new_color):
#         self.color= new_color
#
#
#
# car1 = Car('Logan', 'alb')
# car2 = Car('Duster', 'portocaliu')
#
#
# print(car1.color)
# print(car2.color)
#
# car1.accelerate()
# car2.accelerate()
#
# car1.paint('rosuuuuu')
# print(car1.color)
# print(car2.color)


class Nerfgun:
    # atribute/fields
    model = None
    nr_gloante = 0
    piedica_pusa = True
    culoare = None
    culoriposibile = {'alb', 'negru', 'rosu'}
    # constructor

    def __init__(self, model, culoare):
        self.model = model
        if culoare in self.culoriposibile:# trebuie sa preluam cu self.
            self.culoare = culoare
        else:
            print(f'La initializarea obiectului {model}, culoarea este invalida')

    # metode
    def descrie(self):
        print(f'Modelul este {self.model}')
        print(f'nr de gloante  este {self.nr_gloante}')
        print(f'piedica  este {self.piedica_pusa}')
        print(f'culoarea este este {self.culoare}')

    def scoate_piedica(self):
        self.piedica_pusa = False
        print('Ai scos piedica cu succes!')
    def incarca(self, nr_gloante):
       if nr_gloante >10:
           self.nr_gloante = 10
       else:
           self.nr_gloante = nr_gloante

    def trage(self):
        if self.nr_gloante > 0 and self.piedica_pusa == False:
            self.nr_gloante-=1
            print('Pac Pac')
        # elif nr_gloante <=0:
        #     print('Nr de gloante invalide')
        else:
            print('Nu poti trage, verifica piedica scoasa si nr de gloante')


#initializam obiecte
nerf1 = Nerfgun('Glock', 'alb')
nerf2 = Nerfgun('Deagle', 'roz')


nerf1.descrie()
nerf2.descrie()
# Culoare invalida# merge pe else
# Modelul este Glock
# nr de gloante  este 0
# piedica  este True
# culoarea este este alb
# Modelul este Deagle
# nr de gloante  este 0
# piedica  este True
# culoarea este este None
nerf2.culoare = 'verde'# suprascriere atribute
nerf2.descrie()
nerf1.scoate_piedica()
nerf1.trage()
# nerf1.incarca(-5)
# nerf1.incarca(11)
nerf1.incarca(5)
nerf1.scoate_piedica()
nerf1.trage()
nerf1.descrie()





class Caine:
    rasa = None
    nume = None
    culoare = None
    nume_stapan = None
    def __init__(self, rasa):
        self.rasa = rasa
grivei = Caine('golden')
print(grivei.rasa)