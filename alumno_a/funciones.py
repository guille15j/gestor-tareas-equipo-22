from colorama import init, Fore, Style

init()

def mostrar_menu():
    """Muestra el menú principal y devuelve la opción elegida."""
    opcion = -1
    
    print(f"\n{Fore.CYAN}=== GESTOR DE TAREAS ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}1{Style.RESET_ALL}. Ver tareas")
    print(f"{Fore.YELLOW}2{Style.RESET_ALL}. Añadir tarea")
    print(f"{Fore.YELLOW}3{Style.RESET_ALL}. Marcar tarea como completada")
    print(f"{Fore.YELLOW}4{Style.RESET_ALL}. Eliminar tarea")
    print(f"{Fore.YELLOW}5{Style.RESET_ALL}. Salir")

    
    while opcion not in [1,2,3,4,5]:
        try:
            opcion = input(f"\n{Fore.YELLOW}Elige opción: {Style.RESET_ALL}")
            opcion = int(opcion)

            if opcion not in [1, 2, 3, 4, 5]: print(f"{Fore.RED}Opción fuera de rango. Debe estar dentro del rango de opciones.{Style.RESET_ALL}")

        except ValueError: 
            print(f"{Fore.RED}Debes introducir un número entero válido.{Style.RESET_ALL}")

    return opcion

def ver_tareas(fichero):
    """Muestra todas las tareas numeradas."""
    # TODO: Implementar
    pass

def añadir_tarea(fichero):
    """Añade una nueva tarea al fichero."""
    # TODO: Implementar
    pass

mostrar_menu()