from colorama import init, Fore, Style
init()

def mostrar_menu():
    """Muestra el menú principal y devuelve la opción elegida."""
    # TODO: Implementar
    pass

def ver_tareas(fichero):
    """Muestra todas las tareas numeradas."""
    # TODO: Implementar
    pass

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
