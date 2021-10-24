from modules import commands_balanceador as commands
from os import system

#Definir tablas de rutas y prioridad
rt_tables = open(commands.PATH_ROUTES)
content = rt_tables.read()
content += "2   T0\n"
content += "3   T1"
rt_tables.write(content)
rt_tables.close()

#funciones
def ejecutar_command(comando):
    try:
        print("Ejecutando... ",comando)
        system(comando)
        print("\n")
    except:
        print("Error")
#crear enrutamiento

ejecutar_command(commands.R1)
ejecutar_command(commands.R2)
ejecutar_command(commands.R3)
ejecutar_command(commands.R4)
ejecutar_command(commands.R5)
ejecutar_command(commands.R6)
ejecutar_command(commands.P1)
