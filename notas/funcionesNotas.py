import notas.modeloNotas as ModeloNotas

def buscarTitulo(titulo):
    buqueda=ModeloNotas.Notas.buscarTitilo(titulo)
    return buqueda
def registroNuevaNota(idUsuario):
    print('\n          Datos de la nota')
    titulo = input('Titulo de la nota: ')
    descripcion = input('Descripcion: ')
    validacioTitulo=buscarTitulo(titulo)
    if len(validacioTitulo)!=0:
        return '¡Up! ya exste un nota con este titulo'
    else:
        try:
            nota = ModeloNotas.Notas(idUsuario,titulo,descripcion)
            guardar = nota.guardar()
            return guardar
        except:
           return 'Error al registrar nota en la bd' 
def mostrarTodas():
    print('\n------- Listado de Notas registradas---------')
    buscando = ModeloNotas.Notas.buscarTodo()
    return buscando

def eliminarNota(titulo):
    buscando = buscarTitulo(titulo)
    if len(buscando)==0:
        print(" La nota nota no existe 😢" )
    else:
        try:
            eliminar =ModeloNotas.Notas.eliminarNota(titulo)
            return eliminar
        except:
            return 'Error al eliminar la nota en la bd'
