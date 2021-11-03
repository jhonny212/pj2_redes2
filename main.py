def obtener_notas():
    data1 = open('pesos.txt').read()
    obj = data1.replace('ISP1=','').replace('ISP2=','').split('\n')
    return obj[0],obj[1]

def obtener_conf_clientes():
    data1 = open('LBrules.txt').read()
    data1 = data1.splitlines()
    instrucciones = []
    for x in data1:
        instrucciones.append(x.split(','))
    return instrucciones

#datos de ISP
ISP1_UP = input("Escriba la velocidad de subida para el ISP1 \n")
ISP1_DOWN = input("Escriba la velocidad de bajada para el ISP1 \n")
ISP2_UP = input("Escriba la velocidad de subida para el ISP2 \n")
ISP2_DOWN = input("Escriba la velocidad de bajada para el ISP2 \n")

#datos balanceo de carga
ISP1,ISP2=obtener_notas()

#datos para LBrules   
LB_RULES=obtener_conf_clientes()