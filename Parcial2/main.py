import crud.CRUD as CRUD
import ui
import os
import subprocess
subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)

while True:
    subprocess.run('clear' if os.name == 'posix' else 'cls', shell=True)
    print("Menú de opciones:")
    print("1. Crear un nuevo cliente")
    print("2. Buscar un cliente por su cédula")
    print("3. Actualizar el nombre de un cliente")
    print("4. Eliminar un cliente")
    print("5. Crear un nuevo pedido")
    print("6. Buscar un pedido por cedula")
    print("7. Pagar un pedido")
    print("8. Actualizar un pedido")
    print("9. Eliminar un pedido")
    print("10. Salir")

    opcion = int(input("Ingrese la opción que desea ejecutar: "))

    if opcion == 1:
        ui.ui_cliente_nuevo()
        
    elif opcion == 2:
        ui.ui_buscar_cliente()

    elif opcion == 3:
        ui.ui_actualizar_cliente()

    elif opcion == 4:
        ui.ui_eliminar_cliente()

    elif opcion == 5:
        ui.ui_crear_pedido()

    elif opcion == 6:
        ui.ui_buscar_pedido()

    elif opcion == 7:
        ui.ui_pagar_pedido()

    elif opcion == 8:
        ui.ui_actualizar_pedido()

    elif opcion == 9:
        ui.ui_eliminar_pedido()

    elif opcion == 10:
        break

    else:
        print("Opción inválida, por favor ingrese una opción válida.")
