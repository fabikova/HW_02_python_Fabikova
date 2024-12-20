import json
import math

# otvorenie súboru a načítanie dát
with open("netflix_titles.tsv", mode="r", encoding="utf-8") as netflix_titles:
    netflix_titles.readline()  # preskočí prvý riadok (hlavičku)

    netflix_list = []  # zoznam na ukladanie slovníkov

    # prechádzanie cez všetky riadky v súbore okrem prvého
    for line in netflix_titles:
        value_movie = line.strip().split('\t')  # odstránenie bielych miest a rozdelenie riadku podľa tabulátora

        movie_dict = {}  # slovník pre každý film

        title = value_movie[2]  # PRIMARYTITLE
        directors = value_movie[15]  # DIRECTOR
        cast = value_movie[16]  # CAST
        genres = value_movie[8]  # GENRES
        start_year = value_movie[5]  # STARTYEAR


        def dictionary_add(movie_dict, key, value):
            movie_dict[key] = value.split(', ') if value else []

        # Použitie funkcie dictionary_add na pridanie hodnôt do slovníka
        dictionary_add(movie_dict, 'title', title)
        dictionary_add(movie_dict, 'directors', directors)
        dictionary_add(movie_dict, 'cast', cast)
        dictionary_add(movie_dict, 'genres', genres)

        # prepočet rokov na desaťročia, priradenie hodnôt do slovníka
        if start_year:
            start_year_int = int(start_year)
            movie_dict['decade'] = math.floor(start_year_int / 10) * 10
        else:
            movie_dict['decade'] = []

        # pridanie filmu do zoznamu
        netflix_list.append(movie_dict)

# uloženie do JSON
with open('hw02_output.json', 'w', encoding='utf-8') as json_file:
    json.dump(netflix_list, json_file, ensure_ascii=False, indent=4)


