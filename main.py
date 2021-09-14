import usuarios.funcionesUsuario as  funcionesDeUsuario
import notas.funcionesNotas as operacionesNoatas

def iniciar():
    print('     Hola Bienvenido Al Sistema de Administracion De Notas ADSI')
    print('Que deseas hacer?  \n   1. registrarme \n   2. Iniciar sesion \n Puedes digitar los numeros 1 o 2 de del menú  ' )
    opcion=input('Ingresa la accion que deseas relizar:')
    if opcion=='1':
         registrarUser = funcionesDeUsuario.usuarioNuevo()
         print(registrarUser)
    elif opcion=='2':
        login=funcionesDeUsuario.login()
        if login[0]!=True:
            print(login)
        else:
            idUsuario=login[2]
            print(f'\n        Bienvenido {login[1]}     ')
            accion=''
            while accion !='4':
                print('\n        menu   ')
                print('   1. Crear nota  \n   2. Mostrar Notas  \n   3. Eliminar nota  \n   4. Salir ')
                accion = input('Por favor ingrese una occion del menu ejemplo 1,2,3,4 \n¿Que quieres hacer?:  ')
                if accion=='1':
                    nuevaNota=operacionesNoatas.registroNuevaNota(idUsuario)
                    print(nuevaNota)
                elif accion=='2':
                    notas=operacionesNoatas.mostrarTodas()
                    print(notas)
                elif accion=='3':
                    notas=operacionesNoatas.mostrarTodas()
                    for nota in notas:
                        print(f'{nota[2]}')
                    notaEliminada = input("¿Cual nota va a eliminar?: ")
                    eliminar = operacionesNoatas.eliminarNota(notaEliminada)
                    print(eliminar)
                elif accion=='4':
                    print('Adios🙌 \nMuchas gracias por usar nuetro sistema')
                elif opcion=='':
                    print('No elegiste ninguna opcion')
                else:
                    print('La opcion ',accion,' ingresada no es valida')
    elif opcion=='':
        print('No elegiste ninguna opcion 🥱')
    else:
        print('La opcion ',opcion,' ingresada no es valida 😑')



# ejecuta el proyecto
iniciar()