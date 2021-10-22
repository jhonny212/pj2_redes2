from os import system
from modules import commands

#funciones
def ejecutar_command(comando):
    try:
        print("Ejecutando... ",comando)
        system(comando)
        print("\n")
    except:
        print("Error")

#configurar isp
ISP_UP = f"ip addr add 10.10.10.1/24 dev {commands.INTERFACE_IN}"
ISP_DOWN = f"ip addr add 10.10.10.2/24 dev {commands.INTERFACE_OUT}"

ejecutar_command(ISP_UP)
ejecutar_command(ISP_DOWN)
ejecutar_command(commands.C1)
ejecutar_command(commands.C2)
ejecutar_command(commands.C3)
ejecutar_command(commands.C4)
ejecutar_command(commands.C5)
ejecutar_command(commands.C6)
ejecutar_command(commands.COMANDO_IN_ROOT)
ejecutar_command(commands.COMANDO_IN_ENLACE)
ejecutar_command(commands.COMANDO_OUT_ROOT)
ejecutar_command(commands.COMANDO_OUT_ENLACE)
ejecutar_command(commands.DOWNLOAD)
ejecutar_command(commands.UPLOAD)