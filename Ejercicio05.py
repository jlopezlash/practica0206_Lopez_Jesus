#Escribir un programa que cree un diccionario de traducción español-inglés.
#El usuario introducirá las palabras en español e inglés separadas por dos puntos,
#y cada par <palabra>:<traducción> separados por comas, hasta que el usuario
#introduzca la palabra “terminar”. El programa debe crear un diccionario con las palabras
#y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para
#traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
Tra = {}
A = input('Introdicir palabra:traduccion'
           ' y estas separadas por comas al final poner terminar ')
A = A.split(',')
A.pop(-1)
for i in range(len(A)):
    clave,valor = A[i].split(':')
    Tra[clave] = valor
Frase = (input('Dime una frase en español ')).capitalize()
Frase = Frase.split()
for i in Frase:
    if i in Tra:
        print(Tra[i])
    else:
        print(i)