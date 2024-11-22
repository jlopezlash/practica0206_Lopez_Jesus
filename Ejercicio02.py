#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
#y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje “<nombre> tiene <edad> años,
#vive en <dirección> y su número de teléfono es <teléfono>”.
claves = ['Nombre', 'Edad', 'Dirección', 'Telefono']
Datos = {}
for clave in claves:
    Datos[clave] = input('Dime tu ' + clave + ' ')
print(Datos['Nombre'], 'tiene ' + Datos['Edad'], 'años, vive en '
       + Datos['Dirección'], 'y su número de teléfono es ' + Datos['Telefono'])