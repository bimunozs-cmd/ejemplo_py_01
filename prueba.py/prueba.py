
usuario = []

edades = []

print("hola soy nuevo")


cantidad = int(input("Cuantos usuarios quiere ingresar?: "))

for i in range(cantidad):

    nombre = str(input("ingrese su nombre ="))

    usuario.append(nombre)



    saludar = print(f"hola {nombre} good day")

    edad = int(input(f"porfavor {nombre} ingresa tu edad ="))

    edades.append(edad)




for usr in usuario:


    print(usr)

for ed in edades :

    print(ed)







