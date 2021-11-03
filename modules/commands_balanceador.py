PATH_ROUTES = '/etc/iproute2/rt_tables'

#tabla de enrutamiento
C1 = "ip route add 10.10.10.0/24 dev enp7s0 src 10.10.10.3 table T0"
C2 = "ip route add default via 10.10.10.1 table T0"

C3 = "ip route add 10.10.20.0/24 dev enp7s0 src 10.10.20.3 table T1"
C4 = "ip route add default via 10.10.20.1 table T1"

#IPTABLES
C5 = "iptables -t mangle -A PREROUTING -j CONNMARK --restore-mark"
C6 = "iptables -t mangle -A PREROUTING -m mark ! --mark 0 -j ACCEPT"
C7 = "iptables -t mangle -A PREROUTING -j MARK --set-mark 3"
C8 = ""
C9 = "iptables -t mangle -A PREROUTING -j CONNMARK --save-mark"
C10 = "iptables -t nat -A POSTROUTING -j MASQUERADE"
C11 = "ip rule add fwmark 3 table T0 prio 33000"
C12 = "ip rule add fwmark 4 table T1 prio 33000"
C13 = "ip route del default"

def get_percentage(total,enp7s0):
    global C8
    perc = 1-(total/enp7s0)
    C8 = f"iptables -t mangle -A PREROUTING -m statistic --mode random --probability {perc} -j MARK --set-mark 4"