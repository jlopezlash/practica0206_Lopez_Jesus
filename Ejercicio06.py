Alumnos = {}
P = ['NIF','Nombre','Edad','Sexo','Teléfono','Correo']
Opc = ''
while Opc != '6':         #Voy ha dar opciones en un menú de la siguiente manera
    print('''
        1)Añadir alumno         4)Listar todo el alumnado               
        2)Eliminar alumno       5)Listar alumnado aprobado
        3)Mostrar alumno        6)Terminar
          ''')
    Opc = input('Seleccione una opción: ')
    if Opc == '1':
        nif = input('Dime su NIF ')
        nombre = input('Dime su nombre ')
        edad = int(input('Dime su edad '))
        sexo = input('Dime su sexo ')
        telefono = input('Dime su telefono ')
        correo = input('Dime su correo ')
        aprobado = input('Esta aprobado (Si/No)')
        alumno = {'nombre':nombre, 'edad':edad, 'sexo':sexo,
                  'telefono':telefono, 'correo':correo, 'aprobado':aprobado }
        Alumnos[nif] = alumno
    if Opc == '2':
        nif = input('Dime el nif ')
        if nif in Alumnos:
            del alumno[nif]
        else:
            print('No aparece el alumno con el nif ' + nif)
    if Opc == '3':
        nif = input('Dime el nif ')
        for clave, valor in Alumnos[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No aparece el alumno con el nif ' + nif)
    if Opc == '4':
        print('Lista de alumnos')
        for clave, valor in Alumnos.items():
            print(clave, valor['nombre'])
    if Opc == '5':
        print('Lista de clientes aprobados')
        for clave, valor in Alumnos.items():
            if valor['aprobado']:
                print(clave, valor['nombre'])