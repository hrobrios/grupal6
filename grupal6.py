import json

class Proveedor:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

    def registrar_venta(self, monto_venta):
        with open('registro_ventas.txt', 'a') as file:#agregar append "a"
            file.write(str(monto_venta) + '\n')

    def calcular_comision(self):
        with open('registro_ventas.txt', 'r') as file:#lectura "r"
            ventas = file.readlines()
            total_ventas = sum([int(venta.strip()) for venta in ventas])
            comision = total_ventas * 0.1
            return comision

proveedor = Proveedor('usuario', 'contraseña')
proveedor.registrar_venta(100)
proveedor.registrar_venta(75)

comision = proveedor.calcular_comision()
print('Comisión del proveedor:', comision)

