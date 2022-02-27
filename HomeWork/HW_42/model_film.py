import os.path
import pickle


class Film:
    def __init__(self, title, style, director, year, duration, studio, actors):
        self.title = title
        self.style = style
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f'{self.title} ({self.director})'


class FilmModel:
    def __init__(self):
        self.dict_film = 'film_catalog.txt'
        self.catalog = self.load_data()

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.catalog[film.title] = film

    def get_all_films(self):
        return self.catalog.values()

    def get_single_film(self, user_title):
        film = self.catalog[user_title]
        dict_film = {
            'название': film.title,
            'жанр': film.style,
            'режиссер': film.director,
            'год выпуска': film.year,
            'продолжительность': film.duration,
            'студия': film.studio,
            'актеры': film.actors

        }
        return dict_film

    def load_data(self):
        if os.path.exists(self.dict_film):
            with open(self.dict_film, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.dict_film, 'wb') as f:
            pickle.dump(self.catalog, f)

    def remove_film(self, user_title):
        return self.catalog.pop(user_title)
