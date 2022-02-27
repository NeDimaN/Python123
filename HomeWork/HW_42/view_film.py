def add_title(title):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            print(f'{title.center(50, "=")}')
            output = function(*args, **kwargs)
            print('=' * 50)
            return output

        return wrapper

    return real_decorator


class UserInterface:
    @add_title(' Редактирование данных каталога фильмов ')
    def wait_user_answer(self):
        print('Действия с фильмами:')
        print('1 - добавление фильма'
              '\n2 - каталог фильмов'
              '\n3 - просмотр определенного  фильма'
              '\n4 - удаление фильма'
              '\nq - выход из программы')
        user_answer = input('Выберите вариант действия: ')

        return user_answer

    @add_title(' Добавление фильма: ')
    def add_user_films(self):
        dict_film = {
            'название фильма': None,
            'жанр': None,
            'режиссер': None,
            'год выпуска': None,
            'продолжительность': None,
            'студия': None,
            'актеры': None
        }
        for key in dict_film:
            dict_film[key] = input(f'введите {key} фильма: ')

        return dict_film

    @add_title(' Каталог фильмов: ')
    def show_all_films(self, films):
        for ind, film in enumerate(films, 1):
            print(f'{ind}. {film}')

    @add_title(' Ввод названия фильма :')
    def get_user_film(self):
        user_film = input('Введите название фильма:')
        return user_film

    @add_title('Сообщение об ошибке')
    def show_incorrect_title_error(self, user_title):
        print(f'Фильма с названием "{user_title}" в каталоге не существует')

    @add_title('Просмотр определенного фильма:')
    def show_single_film(self, film):
        for key in film:
            print(f'{key} фильма - {film[key]}')

    @add_title('Сообщение об ошибке ввода')
    def show_incorrect_answer_error(self, answer):
        print(f' Варианта "{answer}" не существует!')

    @add_title('Удаление фильма')
    def remove_single_film(self, film):
        print(f'Фильм "{film}" - был удален')
