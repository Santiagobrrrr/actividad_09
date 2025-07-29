movies = []

def info_movie(movie_title, release_movie, movie_genre):
    general_info = [movie_title, release_movie, movie_genre]
    movies.append(general_info)

def display_movies():
    if len(movies) != 0:
        for movie in movies:
            print(f"\n -- {movie[0].upper()} --")
            print(f"Año de estreno de película: {movie[1]}")
            print(f"Género de película: {movie[2]}\n")
    else:
        print("No hay películas registradas\n")

def search_movie(genre_user):
    print(f"\nPelículas encontradas con el género {genre_user}:")
    count = 0
    for movie in movies:
        if movie[2] == genre_user:
            print(f"{movie[0].upper()}: {movie[1]}")
            count += 1
    if count == 0:
        print(f"No hay ninguna película con ese género.")
    print("")

def delete_movie(title_user):
    for movie in movies:
        if title_user == movie[0]:
            movies.remove(movie)
            print(f"Película eliminada exitosamente\n")
        else:
            print(f"Película no encontrada\n")

def show_statistics():
    if len(movies) == 0:
        print("No hay películas registradas para mostrar estadísticas.\n")

    print(f"Cntidad total de películas registradas: {len(movies)}")

    genre_count = {}

    for movie in movies:
        genre = movie[2]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1

    print("\nPelículas por género:")
    for genre, count in genre_count.items():
        print(f" - {genre}: {count}")

    oldest_movie = movies[0]
    for movie in movies:
        if movie[1] < oldest_movie[1]:
            oldest_movie = movie

    print(f"\nPelícula más antigua registrada:")
    print(f" - {oldest_movie[0].upper()} ({oldest_movie[1]}) - Año de estreno: {oldest_movie[1]}\n")

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
                movie_title = input(f"Ingrese el titulo de la película {(i+1)}: ").lower()
                release_movie = int(input(f"Ingrese el año de estreno {i+1}: "))
                movie_genre = input(f"Ingrese el género de la película {i+1}: ").lower()
                info_movie(movie_title, release_movie, movie_genre)

        case "2":
            print(f"\nPelículas registradas:")
            display_movies()

        case "3":
            print(f"\nBuscar películas según su género")
            genre_user = input(f"Ingrese un género de película: ").lower()
            search_movie(genre_user)

        case "4":
            print(f"\nEliminar película")
            title_user = input(f"Ingrese el nombre de la película a eliminar: ").lower()
            delete_movie(title_user)

        case "5":
            print(f"\nVer estadística")
            show_statistics()

        case "6":
            print(f"\nSalió del menú, gracias por su visita")
            break

        case _:
            print(f"\nOpción inválida, intente de nuevo")