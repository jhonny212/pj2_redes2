#interfacez
INTERFAZ_DOWNLOAD_ISP1 = 'enp1s0'
INTERFAZ_DOWNLOAD_ISP2 = 'enp7s0'
INTERFAZ_UPLOAD_ISP1 = 'ibf0'
INTERFAZ_UPLOAD_ISP2 = 'ibf1'

#ips
IP_DOWNLOAD_ISP1 = '10.10.10.3'
IP_DOWNLOAD_ISP2 = '20.20.20.3'
IP_UPLOAD_ISP1 = ''
IP_UPLOAD_ISP2 = ''

#GTW
GTW1 = '10.10.10.1'
GTW2 = '20.20.20.1'

#Subred
SUBRE1 = '10.10.10.0/24'
SUBRE2 = '20.20.20.0/24'

PATH_ROUTES = '/etc/iproute2/rt_tables'

#Rutas de encaminamiento
R2 = f'ip route add default dev {INTERFAZ_DOWNLOAD_ISP1} via {GTW1} table T0'
R1 = f'ip route add {SUBRE1} dev {INTERFAZ_DOWNLOAD_ISP1} src {IP_DOWNLOAD_ISP1} table T0'

R4 = f'ip route add default dev {INTERFAZ_DOWNLOAD_ISP2} via {GTW2} table T1'
R3 = f'ip route add {SUBRE2} dev {INTERFAZ_DOWNLOAD_ISP2} src {IP_DOWNLOAD_ISP2} table T1'

#Reglas de encaminamiento
R5 = f'ip rule add from {IP_DOWNLOAD_ISP1}/32 table T0'
R6 = f'ip rule add to {IP_DOWNLOAD_ISP1}/32 table T0'

R7 = f'ip rule add from {IP_DOWNLOAD_ISP2}/32 table T1'
R8 = f'ip rule add to {IP_DOWNLOAD_ISP2}/32 table T1'

#Configuracion de pesos
P1 = f'ip route add default scope global nexthop via '
P1+= f'{GTW1} dev {INTERFAZ_DOWNLOAD_ISP1} weight 1 nexthop via '
P1+= f'{GTW2} dev {INTERFAZ_DOWNLOAD_ISP2} weight 1'
