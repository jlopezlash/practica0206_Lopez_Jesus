#Escribir un programa que guarde en un diccionario los precios
#de los artículos de la tabla, pregunte al usuario por un artículo,
#un número de unidades y muestre por pantalla el precio de esa cantidad de producto.
#Si el producto no está en el diccionario debe mostrar un mensaje informando de ello.
Articulo = {'Pan':1.40, 'Huevos':2.30, 'Cebolla':0.85, 'Aceite':4.35}
A = input('Dime un articulo ')
B = int(input('Dime las unidades '))
C = Articulo.get(A, 'No hay')
if C == 'No hay':
    print(C)
else:
    print(round((C * B),3))