#Variables
INTERFACE_IN = 'enp7s0'
INTERFACE_OUT = 'enp8s0'
IP = '10.10.10.2'

#reglas de filtros a aplicar para ancho de banda de subida como de bajada
IN=f"tc filter add dev {INTERFACE_IN} parent 1:0 protocol ip prio 1 u32 match ip dst "
OUT=f"tc filter add dev {INTERFACE_OUT} parent 1:0 protocol ip prio 1 u32 match ip src "
PUERTO="match ip sport "
REGLA="0xffff flowid"

#insertar modulo ifb, asignando el numero de interfacez virtuales 
# que se necesita por defecto es 2
IFB = "modprobe ifb numifbs=1"

#hablitar interfaz para upload
C1 = f"ip link set dev {INTERFACE_OUT} up"
C2 = f"tc qdisc del dev {INTERFACE_IN}root 2>/dev/null"
C3 = f"tc qdisc del dev {INTERFACE_IN}ingress 2>/dev/null"
C4 = f"tc qdisc del dev {INTERFACE_OUT} root 2>/dev/null"
C5 = f"tc qdisc add dev {INTERFACE_IN}handle ffff: ingress"
C6 = f"""tc filter add dev {INTERFACE_IN}parent ffff: protocol ip u32 match u32 0 0 
action mirred egress redirect dev $INTERFACE_OUT"""

#creando enlance para bajada
COMANDO_IN_ROOT = f"tc qdisc add dev {INTERFACE_IN}root handle 1: htb"
COMANDO_IN_ENLACE = f"tc class add dev {INTERFACE_IN}parent 1: classid 1:11 htb rate 1mbit"

#Creando enlace para subida
COMANDO_OUT_ROOT = f"tc qdisc add dev {INTERFACE_OUT} root handle 1: htb"
COMANDO_OUT_ENLACE = f"tc class add dev {INTERFACE_OUT} parent 1: classid 1:11 htb rate 1024kbit"


#asignano ip a enlace
DOWNLOAD = f"{IN} {IP} {PUERTO} 3128 {REGLA} 1:11"
UPLOAD = f"{OUT} {IP} flowid 1:11"