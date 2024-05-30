Dic_user={
    "VICCOS":"12345",
    "VICCAS":"9876",
    "BASROJ":"6543"
}
while True:
    usuario=""
    usuario=input("Ingrese clave a buscar\n")
    if Dic_user.get(usuario,"No existe")=="No existe":
        print("Usuario no existe")
    else:
        print("Usuario Existe")
        break