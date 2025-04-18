from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_name_longer_than_limit_add_zero_books(self):

        collector = BooksCollector()
        collector.add_new_book('Очень длинное название книги, 42 символа!!')

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_is_empty_value(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert collector.get_books_genre()['Гордость и предубеждение и зомби'] == ''

    def test_dict_books_genre_is_empty(self):

        collector = BooksCollector()
        assert len(collector.books_genre) == 0

    def test_list_favorites_is_empty(self):

        collector = BooksCollector()
        assert len(collector.favorites) == 0

    def test_list_genre_true(self):

        collector = BooksCollector()
        assert  collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_list_genre_age_rating_true(self):
        collector = BooksCollector()
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_set_book_genre_add_genre_true(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Ужасы'

    def test_set_book_genre_add_book_with_empty_genre_none_genre(self):

        collector = BooksCollector()
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') is None

    def test_set_book_genre_add_wrong_genre_is_empty(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Романтика')

        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == ''

    def test_get_books_with_specific_genre_true(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детектив')
        collector.add_new_book('Кошмар на улице Вязов')
        collector.set_book_genre('Кошмар на улице Вязов', 'Ужасы')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Что делать, если ваш кот хочет вас убить', 'Кошмар на улице Вязов']

    def test_get_books_with_specific_genre_with_other_genre_is_empty(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детектив')
        collector.add_new_book('Кошмар на улице Вязов')
        collector.set_book_genre('Кошмар на улице Вязов', 'Ужасы')

        assert collector.get_books_with_specific_genre('Мультфильмы') == []

    def test_get_books_with_specific_genre_with_wrong_genre_is_empty(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детектив')
        collector.add_new_book('Кошмар на улице Вязов')
        collector.set_book_genre('Кошмар на улице Вязов', 'Ужасы')

        assert collector.get_books_with_specific_genre('Романтика') == []

    def test_get_books_for_children_true(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детектив')
        collector.add_new_book('Сказка о рыбаке и рыбке')
        collector.set_book_genre('Сказка о рыбаке и рыбке', 'Мультфильмы')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_new_book('Мистер пропер')
        collector.set_book_genre('Мистер пропер', 'Комедии')

        assert collector.get_books_for_children() == ['Сказка о рыбаке и рыбке', 'Властелин колец', 'Мистер пропер']

    def test_get_books_for_children_with_not_accessible_genre_is_empty(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_add_favorite_book_true(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == ['Что делать, если ваш кот хочет вас убить']

    def test_add_book_in_favorites_not_add_favorite_book_is_empty(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_add_favorite_and_not_favorite_books_just_favorite_book(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == ['Что делать, если ваш кот хочет вас убить']

    def test_delete_book_from_favorites_delete_correct_book_delete_correct_book(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == ['Властелин колец']

    def test_delete_book_from_favorites_delete_wrong_book_nothing_delete(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert collector.get_list_of_favorites_books() == ['Что делать, если ваш кот хочет вас убить', 'Властелин колец']
