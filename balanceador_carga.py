from modules import commands_balanceador

#Definir tablas de rutas y prioridad
rt_tables = open(commands_balanceador.PATH_ROUTES)
content = rt_tables.read()
content += "2   T0\n"
content += "3   T1"

#crear enrutamiento

