# 1. Display the sum of 5 + 10, using two variables: x and y.
x = 5
y = 10
print(x+y)


# 2. Creați cȃte o variabilă de tipul: string, int și float, după cum urmează:
# Variabila de tip int va reține valoarea 20.
# Variabila de tip float va reține valoarea 10.
# Variabila de tip string reține valoarea "python".
a = 20
b = 20.10
c = 'python'
print(type(a))
print(type(b))
print(type(c))

# 3. Utilizȃnd funcția type, determinați tipul următoarelor variabile:
# restanta = 0
# notaFinala = 10.0
# laborator = "Introducere in informatica"

restanta = 0
notaFinala = 10.0
laborator = 'introducere in informatica'
print(type(restanta))
print(type(notaFinala))
print(type(laborator))

# 4. Verificaţi dacă un cuvânt este palindrom. Un cuvânt este palindrom dacă scris de la dreapta la
# stanga, este tot acel cuvânt.(folositi assert pt verificare)

palindrom = input('introdu un cuvant')
assert (palindrom == palindrom[::-1])
print('Cuvantul ales este palindrom')

# 5. Remove first n characters from a string (n il cititi de la tatatura)
# "Ana are mere" daca n=3 va afisa " are mere"

fraza = 'Alexandra invata sa elimine caractere dintr-un string'
print(len(fraza))
n = int(input('introdu numarul de caractere pe care vrei sa le elimini n= '))
print(fraza[n:])


# 5.reads two numbers and multiplies them together and print out their product
q = int(input('primul numar'))
w = int(input('al doilea numar'))
print(q*w)

# 6.Check if the first and last number of a string  is the same. stringul il cititi de la tastatura
string= input('introdu un cuvant')
print(len(string))
print(string[0])
last_index = len(string) -1
print(string[last_index])
assert string[0] == string[last_index]



# 7. Write a program to find how many times substring "Emma" appears in the given string.
str_x = "Emma is good developer. Emma is a writer"
print(str_x.count('Emma'))

# 8. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#pt "eu merg la mare" sa imi afiseze "eure"
string = 'eu merg la mare'
print(len(string)) # numaram caracterele, incepe de la 0, deci  01234
last_index = len(string) # aflam ultimul caracter
penultimul = len(string)-2 # aflam penultimul caracter
print(string[0:2]+ string[-2:last_index])
print(string[0:2]+ string[penultimul:last_index])
print(string[0:2]+ string[-2::1])
print(string[-2:last_index])
print(string[penultimul:last_index])
print(string[-2::1])
# verifica logica din spate !!!

# 9. Write a Python program to calculate the length of a string.
#pt "eu merg la mare" ->15
stringul_meu = 'eu merg la mare'
print(len(stringul_meu))


# 10. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
# sample string = 'restart'
#expected result = 'resta$t'
sample = 'rrrrrr'
print(sample[0] + sample[1::].replace('r','$'))


#11. Utilizand tipurile de print pe care vi le-am aratat: afisati in consola I have 1000 dollars so I can buy 3 football for 450.00 dollars.
#pt datele totalMoney = 1000 quantity = 3 price = 450
total_money = 1000
quantity = 3
price = 450
print(str('I have '+ str(total_money) +' dollars so I can buy '+  str(quantity) +' football for ' + str(price) + ' dollars'))

# 12.Build a program to calculate the followings using the input from the user for a, b, c or r
# • triangle area using input
# • rectangle area and perimeter
# • circle area


# 13. Which of the following are valid ways to specify the string literal foo'bar in Python:
print( 'foo\'bar')# • 'foo\'bar'
print("""foo'bar""")
print("foo'bar")
print('foo''bar')
#print('foo'bar')# eroare

# 14.Password checker script
# Define a username getting input from the console
# Define a password getting input from the console
# Display the following message 'The password for user Paul is
# ********* is 9 characters long)

user_name = input('username') # definim user name ok
password = input('password') # definim parola ok
hidden_pass= '*'* len(password)
print(len(hidden_pass)) # vrem sa printam lungimea paroleiok
print(hidden_pass)
# #vrem sa inlocuim parola cu caractere asterix ok
# print(password.replace(password, str(len(password)*'*')))

print('The password for user ' + str(user_name)  +' is ' + hidden_pass + ' is '+ str(len(hidden_pass))+ ' characters long')
#
# de cautat pe net:
# 15.Write a program to take three names as input from a user in the single input() function call.

nume, prenume1, prenume2 = input("Introdu numele tau complet: ").split()
print("Numele de familie: ", nume)
print("Prenume 1 : ", prenume1)
print("Prenume 2 : ", prenume2)

# 16. Display float number with 2 decimal places
a = float(input( 'scrie un numar '))
print(f'{a}')
