import bluetooth

lista = bluetooth.discover_devices(lookup_names = True)
print 'Lista de Dispositivos Bluetooth'
print 'Se encontraron %d' % len(lista)

for hwaddr, nombre in lista:
     print " %s - %s" % (hwaddr,nombre)
