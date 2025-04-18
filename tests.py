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

    def test_add_new_book_add_zero_value(self):

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

    def test_set_book_genre_add_genre_false(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') is None