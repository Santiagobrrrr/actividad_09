while True:
    print(f"+++ MENÚ PELICULAS +++")
    print(f"1. Agregar películas")
    print(f"2. Mostrar películas registradas")
    print(f"3. Buscar películas")
    print(f"4. Eliminar película")
    print(f"5. Ver estadísticas")
    print(f"6. Salir")

    option_user = input(f"Ingrese la opción a la que desea ir: ")
    match option_user:
        case "1":
            print(f"Agregar películas")

        case "2":
            print(f"Películas registradas")

        case "3":
            print(f"Buscar películas según su género")

        case "4":
            print(f"Eliminar películas")

        case "5":
            print(f"Ver estadística")

        case "6":
            print(f"Salir")
            break

        case _:
            print(f"Opción inválida, intente de nuevo")