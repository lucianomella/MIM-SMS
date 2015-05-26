import bluetooth

lista = bluetooth.discover_devices(lookup_names = True)
print 'Lista de Dispositivos Bluetooth'
print 'Se encontraron %d' % len(lista)

for hwaddr, nombre in lista:
	print " %s - %s" % (hwaddr,nombre)
	services = bluetooth.find_service(address=hwaddr)
	if len(services) > 0:
		port = 0
		for svc in services:
			if  svc["name"] == "Dial-Up Networking":
				port = svc["port"]
			if port != 0:
				print "Encontrado Dial-Up Networking port = %d\n" % (port)
