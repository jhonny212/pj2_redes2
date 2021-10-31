from modules import commands_filtro_navegacion as commands
from os import system

def ejecutar_command(comando):
    try:
        print("Ejecutando... ",comando)
        system(comando)
        print("\n")
    except:
        print("Error")

opc = int(input("Desea instalar squid?"))
if opc == 1:
    ejecutar_command(commands.install)

opc = int(input("Desea crear backup?"))
if opc == 1:
    ejecutar_command(commands.cp)

ejecutar_command(commands.deny)
ejecutar_command(commands.allow)

