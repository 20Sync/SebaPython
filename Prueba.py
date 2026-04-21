
# print("Ingrese su nombre")
# nombre=input()
# edad=int(input("Ingrese su edad: "))
# print("Hola", nombre, "su edad en 5 años será", edad+5)

# ========================================

# print("Ingrese el 1er numero: ")
# num1=int(input())
# print("Ingrese el 2do numero: ")
# num2=int(input())

# print("La suma de los dos numeros es: ", num1+num2)
# print("La resta de los dos numeros es: ", num1-num2)

# ========================================

# n1=int(input("Ingrese 1er numero: "))
# n2=int(input("Ingrese 2do numero: "))
# print("La suma de los dos numeros es: ", n1+n2)
# print("La resta de los dos numeros es: ", n1-n2)

# ========================================

#Menu uso del IF

# print(
# '''
# 1.- Pera 1200
# 2.- Manzana 1400
# 3.- Piña 2000

# '''
# )

# select=int(input("Seleccione una opción: "))

# if select==1:
#     print("El total a pagar es: ", 1200*1.19)
# elif select==2:
#     print("El total a pagar es: ", 1400*1.19)
# elif select==3:
#     print("El total a pagar es: ", 2000*1.19)
# else:
#     print("Numero no valido")

# ========================================

#Uso del FOR

# 1)


# for i in range(3):
#     print("Repeticion N ", i+1)


# 2)


# num=int(input("Ingrese un numero: "))

# for i in range (num):
#     print(i+1, "Hola")


# 3)


# num=int(input("Ingrese un numero: "))

# for i in range (10):
#     print(num, " X ", i+1, " = ", num*(i+1))


# 4)


# num=int(input("Ingrese la cantidad de notas: "))
# suma=0
# for i in range(num):
#     nota=float(input("Ingresa la nota: "))
#     suma=suma+nota
# prom=suma/num
# print("El promedio es: ", prom)
# if prom >= 4:
#     print("El alumno aprobó")
# else:
#     print("El alumno reprobó")


# 5)

# for i in "TunTunSahur":
#     print(i)


# 6)


# nom=input("Ingrese su nombre: ")
# cont=nom
# for i in nom:
#     print(i)
#     cont=cont+1
# print("La cantidad de caracteres es: ", cont)


# 7)


# nom=input("Ingrese su nombre: ")
# cont=nom
# cont=0
# for i in nom:
#     if i in "aeiouAEIOU":
#     cont=+1
# print("La cantidad de caracteres es: ", cont)

# ========================================



# num=int(input("Ingrese cantidad de notas: "))
# sum=0
# for i in range (num):
#     notas=float(input(f"Ingrese la nota {i+1}: "))
#     sum=sum+notas
# prom=sum/notas
# print("Promedio: ",round(prom, 1))

# if prom>= 4:
#     print("El alumno aprobo")
# else:
#     print("Alumno reprobó")

# titulo="Clima actual" #Tipo string
# temp=18.6 #float
# DiaDelMes=16 #int
# Mes=4 #int
# Llueve=False

# print(f"{titulo}")
# print(f"Fecha de hoy: {DiaDelMes}-{Mes}")
# print(f"temperatura actual: {temp} Grados")

# if Llueve:
#     print("Saque el paraguas")
# else:
#     print("No saque paraguas")

# num=int(input("Ingrese un numero: "))
# for i in range(num):
#     print(f"{i+1} Hola guatona con moño")


#Pedir nombre al usuario y decirle cuantas letras son


# nom=(input("Ingrese su nombre: "))
# cont=0
# for i in nom:
#     cont=cont+1
# print(f"Su nombre posee: {cont} caracteres")

#Se usa f {variable} para usar una concatenacion dentro de una linea de codigo (print)


#Contar solamente las vocales en un nombre


# nom=(input("Ingrese su nombre: "))
# vocales=0
# for i in nom:
#     # vocales=vocales+1
#     if i in "aeiou" "AEIOU":
#         vocales+=1
# print(f"Su nombre posee: {vocales} vocales")


#Contar solamente las consonantes


# nom=(input("Ingrese su nombre: "))
# consonantes=0
# for i in nom:
#     # vocales=vocales+1
#     if i in "BCDFGHJKLMNÑPQRSTVXZWY" "bcdfghjklmnñpqrstvxzwy":
#         consonantes+=1
# print(f"Su nombre posee: {consonantes} consonantes")


#Vocales y consonantes: 


# nom=(input("Ingrese su nombre: "))
# vocales=0
# cons=0
# for i in nom:
#     # vocales=vocales+1
#     if i in "aeiou" "AEIOU":
#         vocales+=1
#     elif i==" ":
#         print()
#     else:
#         cons+=1
# print(f"Su nombre posee: {vocales} vocales")
# print(f"Su nombre posee: {cons} consonantes")

#Formas de concatenar


# ent1="Seba"
# equip1=6

# ent2="Jairito"
# equip2=4

# print(f"El entrenador {ent1} Tiene {equip1} Pokemons")
# print("El entrenador", ent1,  "Tiene", equip1,  "Pokemons")


#Repeticion de una variable


# print((ent1+" ")*5)


#Caracter


# name="Seba"

# print(name[3])


#Funciones para strings


# name=" Seba "

# print(name.strip()) #Junta los espacios
# print(name.lower()) #Minuscula
# print(name.upper()) #Mayuscula
# print(name.upper().strip()) #Combinacion de ambos
# print(name.replace("Seba", "Tomas")) #Reemplazar string
# print(name.split()) #Hacer lista
# print(name.replace("Seba", "Tomas").split()) #Combinacion de ambos
# print(len(name))


#Ejercicio 1

# clave="SHAZAM"

# pasw=input("Ingrese la clave: ")

# if pasw.upper() == clave:

#     print("Clave Correcta")

# else:
#     print("Clave Incorrecta")


#Ejercicio 2


# nom=input("Ingrese un nombre de usuario: ")

# if len(nom) in range(4,10):
#       print("Sucess")
# else:
#     print("Unsucess")


#Ejercicio 3


# pin=(input("CREE PIN DE 4 DIGITOS: "))

# if len(str(pin)) in range(4, 5):
#      print("Pin creado correctamente")
# else:
#      print("Pin Invalido")

     
# pin=int(input("CREE PIN DE 4 DIGITOS: "))

# if pin> 1000 and pin <9999:
#      print("Pin creado correctamente")
# else:
#      print("Pin Invalido")










