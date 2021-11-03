from modules import commands_balanceador as commands
from os import system

#Definir tablas de rutas y prioridad
rt_tables = open(commands.PATH_ROUTES)
content = rt_tables.read()
content += "2   T0\n"
content += "3   T1"
#rt_tables.write(content)
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



ejecutar_command(commands.C1)
ejecutar_command(commands.C2)
ejecutar_command(commands.C3)
ejecutar_command(commands.C4)
ejecutar_command(commands.C5)
ejecutar_command(commands.C6)
ejecutar_command(commands.C7)
ejecutar_command(commands.C8)
ejecutar_command(commands.C9)
ejecutar_command(commands.C10)
ejecutar_command(commands.C11)
ejecutar_command(commands.C12)
ejecutar_command(commands.C13)



