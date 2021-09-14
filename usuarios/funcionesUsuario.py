import usuarios.modeloUsuario as ModeloUsuarios

def validar(email):
    Busqueda=ModeloUsuarios.Usuario.validar(email)
    return Busqueda
def usuarioNuevo():
    print('Hola Bienvenido\n Por Favor  Ingrese Los  Siguientes Datos Para su Registro')
    nombre = input('Escribe tu nombre: ')
    apellidos = input('Escribe tus apellidos: ')
    email = input('Escribe tu email: ')
    password = input('Escribe tu contraseña: ')
    ValidarEmail= validar(email)
    if len(ValidarEmail)!=0:
        return '¡Up! ya exste un usuario con este email'
    else:
        try:
            usuario = ModeloUsuarios.Usuario(nombre,apellidos,email,password)
            registro = usuario.guardar()
            return registro
        except:
            return 'Error al registrar usuario en la bd'
def login():
    print('Hola Bienvenido Al Inicio de Secion \n Por Favor Ingrese su credenciales')
    email = input('Escribe tu email: ')
    password = input('Escribe tu contraseña: ')
    ValidarEmail= validar(email)
    if len(ValidarEmail)==0:
        return '¡Up! Este usuario no existe'
    else:
        passwordBD = ValidarEmail[0][4]
        if passwordBD!=password:
            return ['¡Nop! Contraseña invalida','']
        else:
            return [True,ValidarEmail[0][1],ValidarEmail[0][0]]

    
