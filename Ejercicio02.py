# En el archivo “Pregunta02.py”, describa (como comentario en Python) qué es una historia de usuario,
#  para qué sirve y escriba un ejemplo de uso. Luego implemente dicha historia de usuario.

# Una historia de usuario es un metodo estrategico y ordenado, que nos sirve para llevar a acabo
# el correcto desarrollo de un trabajo, en el cual describimos detalladamente los requerimientos
# de la aplicacion, asi como para que servira dicha implementacion.

# Ejemplo: /Implementacion de login/
# Como jefe del area de seguridad de una empresa informatica
# Quiero tener un acceso restringido a la informacion de la empresa
# Para salvaguarda informacion valiosa
# 3

us = input("Ingrese usuario a registrar: ")
passw = input("Ingrese contraseña a registrar: ")

print("\n______________________________")
print("\nIniciar sesión: ")
print("\n______________________________")

while True:
    a = input("\nIngrese usuario: ")
    b = input("Ingrese contraseña: ")

    if str(us)==str(a) and str(passw)==str(b):
        print("\n______________________________")
        print("\nSesion iniciada")
        print("\n______________________________")
        break
    else:
        print("\n______________________________")
        print("\nUsuario o contraseña incorrecta")
        print("\n______________________________")