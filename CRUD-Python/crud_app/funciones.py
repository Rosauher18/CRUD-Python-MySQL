def listarCursos(cursos):
    print("\nCursos: \n")
    contador = 1
    for cur in cursos:
        datos ="{0}. Código: {1} | Nombre: {2} ({3} Creditos)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print(" ")

def pedirDatosRegistro():
    codigo = input("Ingrese el código del curso: ")
    nombre = input("Ingrese el nombre del curso: ")
    creditosCorrecto = False
    while not creditosCorrecto:
        creditos = input("Ingrese créditos: ")
        if creditos.isnumeric():
            creditosCorrecto = True
            creditos = int(creditos)
        else:
            print("Créditos incorrectos: Debe ser números únicamente.")
    curso = (codigo, nombre, creditos)
    return curso

def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEditar = input("Ingrese el código del curso a editar: ")
    
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break
            
    if existeCodigo:
        nombre = input("Ingrese el nombre del curso a modificar: ")
        creditosCorrecto = False
        
        while not creditosCorrecto:
            creditos = input("Ingrese créditos a modificar: ")
            if creditos.isnumeric():
                creditosCorrecto = True
                creditos = int(creditos)
            else:
                print("Créditos incorrectos: Debe ser números únicamente.")
                
        curso = (codigoEditar, nombre, creditos)
    else:
        curso = None
        
    return curso



def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEliminar = input("Ingrese el código del curso a eliminar: ")
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break
    if not existeCodigo:
        codigoEliminar = " "
    return codigoEliminar


