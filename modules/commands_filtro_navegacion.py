#comandos para instalar
install = "apt install squid -y"
cp = "cp /etc/squid/squid.conf /etc/squid/squid.backup.conf"
deny = "touch /etc/squid/palabrasprohibidas"
allow = "touch /etc/squid/palabrasaceptadas"
mem_cache = "cache_mem 64 MB"
storage = "cache_dir aufs /var/spool/squid 500 16 256"
red_local = "acl mired src 40.40.40.0/24"
loclahost = "acl localhost src 40.40.40.1/24"
words_deny = "acl def_prohibidas url_regex /etc/squid/bloqueos/palabrasprohibidas"
C1 = "http_access allow mired !def_prohibidas"
C2 = "http_access allow localhost"
C3 = "http_access deny all"

"""
acl https port 443
http_access allow https"""

IPTABLES1 = "iptables -t nat -A PREROUTING -p tcp -s 172.27.1.0/24 --dport 80 -j REDIRECT --to-port 3128"
IPTABLES2 = "iptables -t nat -A PREROUTING -p tcp -s 172.27.1.0/24 --dport 443 -j REDIRECT --to-port 3128"
IPTABLES3 = "iptables -t nat -A POSTROUTING -s 172.27.1.0/24 -d 0.0.0.0/0 -o eth0 -j MASQUERADE"