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
    try:
        with open(fichero, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        
        if not lineas:
            print(f"{Fore.BLUE}No hay tareas en el fichero.{Style.RESET_ALL}")
            return

        i = 1
        for l in lineas:
            secciones = l.split('|')
            tarea = secciones[1].strip()

            if secciones[0] == '1':
                print(f"{i}. {Fore.CYAN}[ ]{Style.RESET_ALL} {tarea}")
            else:
                print(f"{i}. {Fore.GREEN}[✓]{Style.RESET_ALL} {tarea}")

            i += 1

    except FileNotFoundError:
        print(f"{Fore.RED}El archivo no existe todavía.{Style.RESET_ALL}")


def añadir_tarea(fichero):
    """Añade una nueva tarea al fichero con estado pendiente (0)."""
    nueva_tarea = input("Introduce la descripción de la tarea: ").strip()

    if nueva_tarea == "":
        print(f"{Fore.RED}La tarea no puede estar vacía.{Style.RESET_ALL}")
        return

    try:
        with open(fichero, "a", encoding="utf-8") as f:
            f.write(f"0|{nueva_tarea}\n")

    except OSError:
        print(f"{Fore.RED}Error al escribir en el fichero.{Style.RESET_ALL}")
        return
    except FileNotFoundError:
        print(f"{Fore.RED}No se ha podido encontrar el archivo o no existe.{Style.RESET_ALL}")
        return

    print(f"{Fore.GREEN}Tarea añadida correctamente.{Style.RESET_ALL}")

