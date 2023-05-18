import crud.CRUD as CRUD
import os
import subprocess
import random


subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)


def ui_cliente_nuevo():
    cedula = int(input("Ingrese la cédula del cliente: "))
    cliente = CRUD.buscar_cliente(cedula)
    if cliente is None:
        nombre = input("Ingrese el nombre del cliente: ")
        CRUD.crear_cliente(cedula, nombre)
    else:
        print(f"Cliente ya existe")
    input("Presione Enter para continuar...")

def ui_buscar_cliente():
    cedula = int(input("Ingrese la cédula del cliente a buscar: "))
    cliente = CRUD.buscar_cliente(cedula)
    if cliente is None:
        print("No se encontró el cliente")
    else:
        print(f"Cliente encontrado: {cliente[1]}")
        nombres_columnas,factura = CRUD.buscar_factura_cedula(cedula)
        nombres_columnas_str = "    |".join(nombres_columnas)
        if factura:
            print("Factura encontrada:")
            print(nombres_columnas_str)
            for filas in factura:
                columnas = [str(elemento) for elemento in filas]
                columna= "          |".join(columnas)
                print(columna)
        else:
            print("No se encontraron resultados en factura.")

    input("\nPresione Enter para continuar...")

def ui_actualizar_cliente():
    cedula = int(input("Ingrese la cédula del cliente a actualizar: "))
    nombre = input("Ingrese el nuevo nombre del cliente: ")
    CRUD.actualizar_cliente(cedula, nombre)
    input("Presione Enter para continuar...")

def ui_eliminar_cliente():
    cedula = int(input("Ingrese la cédula del cliente a eliminar: "))
    CRUD.eliminar_cliente(cedula)
    input("Presione Enter para continuar...")

def ui_crear_pedido():
    print("Que desea comprar el cliente:")
    print("1.  Productos de Control")
    print("2.  Antibiotico")
    print("3.  Salir")
    opcion = int(input("Ingrese la opcion: "))
    if opcion == 1:
        nombres_columnas, productos = CRUD.leer_productos_control() 
        nombres_columnas_str = "    |".join(nombres_columnas)
        print(nombres_columnas_str)
        for filas in productos:
            columnas = [str(elemento) for elemento in filas]
            columna= "      |".join(columnas)
            print(columna)
        producto_ica = input("Ingrese el registro ica del producto: ")
        cedula = int(input("Ingrese la cédula del cliente que hizo el pedido: "))
        fecha = input("Ingrese la fecha del pedido (formato YYYY-MM-DD): ")

        CRUD.crear_pedido(producto_ica, cedula, fecha, opcion)

    elif opcion == 2:
        nombres_columnas, antibioticos = CRUD.leer_antibioticos() 
        nombres_columnas_str = "    |".join(nombres_columnas)
        print(nombres_columnas_str)
        for filas in antibioticos:
            columnas = [str(elemento) for elemento in filas]
            columna= "      |".join(columnas)
            print(columna)
        antibiotico= input("Ingrese el nombre completo del antibiotico: ")
        cedula = int(input("Ingrese la cédula del cliente que hizo el pedido: "))
        fecha = input("Ingrese la fecha del pedido (formato YYYY-MM-DD): ")
        
        CRUD.crear_pedido(antibiotico, cedula, fecha, opcion)
    else:
        return
    input("Presione Enter para continuar...")

def ui_buscar_pedido():
    cedula = int(input("Ingrese la cedula del cliente que realizo el pedido: "))
    
    nombres_columnas,pedido = CRUD.buscar_pedido(cedula)
    nombres_columnas_str = "    |".join(nombres_columnas)
    if pedido:
        print("pedido encontrado:")
        print(nombres_columnas_str)
        for filas in pedido:
            columnas = [str(elemento) for elemento in filas]
            columna= "          |".join(columnas)
            print(columna)
    input("Presione Enter para continuar...")

def ui_pagar_pedido():
    id_pedido = int(input("Ingrese el ID del pedido a pagar: "))
    CRUD.pagar_pedido(id_pedido)
    input("Presione Enter para continuar...")


def ui_actualizar_pedido():
    id_pedido = int(input("Ingrese el ID del pedido a actualizar: "))
    cedula = int(input("Ingrese la nueva cédula del cliente: "))
    fecha = input("Ingrese la nueva fecha del pedido (formato YYYY-MM-DD): ")
    CRUD.actualizar_pedido(id_pedido, cedula, fecha)
    input("Presione Enter para continuar...")

def ui_eliminar_pedido():
    id_pedido = int(input("Ingrese el ID del pedido a eliminar: "))
    CRUD.eliminar_pedido(id_pedido)
    input("Presione Enter para continuar...")

