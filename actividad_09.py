from platform import release

movies = []

def info_movie(movie_title, release_date, movie_genre):
    general_info = [movie_title, release_date, movie_genre]
    movies.append(general_info)

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
            number_of_movies = int(input(f"\n¿Cuántas películas desea ingresar?: "))
            for i in range (number_of_movies):
                movie_title = input(f"Ingrese el titulo de la película {i+1}: ").lower()
                release_date = input(f"Ingrese el año de estreno {i+1}: ")
                movie_genre = input(f"Ingrese el género de la película {i+1}: ").lower()
                info_movie(movie_title, release_date, movie_genre)

            print(movies)

        case "2":
            print(f"\nPelículas registradas")

        case "3":
            print(f"\nBuscar películas según su género")

        case "4":
            print(f"\nEliminar películas")

        case "5":
            print(f"\nVer estadística")

        case "6":
            print(f"\nSalió del menú, gracias por su visita")
            break

        case _:
            print(f"\nOpción inválida, intente de nuevo")