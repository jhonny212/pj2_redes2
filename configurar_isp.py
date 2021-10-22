from . import commands

#funciones
def ejecutar_command(comando):
    pass
#configurar isp
ISP_UP = f"ip addr add 10.10.10.1/24 dev {commands.INTERFACE_IN}"
ISP_DOWN = f"ip addr add 10.10.10.2/24 dev {commands.INTERFACE_OUT}"

ejecutar_command(ISP_UP)
ejecutar_command(ISP_DOWN)