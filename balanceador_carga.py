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
opc = 1
if opc==1:
    ejecutar_command("ip add del 10.10.10.3/24 dev enp1s0")
    ejecutar_command("ip add add 10.10.10.3/24 dev enp1s0")
    ejecutar_command("ip add del 20.20.20.3/24 dev enp7s0")
    ejecutar_command("ip add add 20.20.20.3/24 dev enp7s0")


ejecutar_command(commands.R1)
ejecutar_command(commands.R2)
ejecutar_command(commands.R3)
ejecutar_command(commands.R4)
ejecutar_command(commands.R5)
ejecutar_command(commands.R6)
ejecutar_command(commands.R7)
ejecutar_command(commands.R8)
#ejecutar_command(commands.P1)
print(commands.P1)
