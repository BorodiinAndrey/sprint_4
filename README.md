Этот проект содержит автоматические тесты для проверки работы класса `BooksCollector`, который управляет списком книг, жанрами и избранным. Тесты написаны с использованием **Pytest**.

---

## ✅ Список тестов

| №  | Название теста | Описание                                                                           |
|----|----------------|------------------------------------------------------------------------------------|
| 1  | `test_add_new_book_add_two_books` | Проверка добавления двух книг.                                                     |
| 2  | `test_add_new_book_name_longer_than_limit_add_zero_books` | Проверка, что книга с названием более 41 символа не добавляется.                   |
| 3  | `test_add_new_book_is_empty_value` | Проверка, что у новой книги по умолчанию жанр — пустая строка.                     |
| 4  | `test_dict_books_genre_is_empty` | Проверка, что словарь книг изначально пустой.                                      |
| 5  | `test_list_favorites_is_empty` | Проверка, что список избранных книг изначально пустой.                             |
| 6  | `test_list_genre_true` | Проверка, что список доступных жанров соответствует ожиданиям.                     |
| 7  | `test_list_genre_age_rating_true` | Проверка, что список возрастных ограничений соответствует ожиданиям.               |
| 8  | `test_set_book_genre_add_genre_true` | Проверка, что жанр корректно добавляется к книге.                                  |
| 9  | `test_set_book_genre_add_book_with_empty_genre_none_genre` | Проверка, что нельзя назначить жанр, если книга не добавлена.                      |
| 10 | `test_set_book_genre_add_wrong_genre_is_empty` | Проверка, что некорректный жанр не сохраняется.                                    |
| 11 | `test_get_books_with_specific_genre_true` | Проверка корректной фильтрации книг по жанру.                                      |
| 12 | `test_get_books_with_specific_genre_with_other_genre_is_empty` | Проверка, что фильтрация по несуществующему жанру возвращает пустой список.        |
| 13 | `test_get_books_with_specific_genre_with_wrong_genre_is_empty` | Проверка, что фильтрация по недопустимому жанру возвращает пустой список.          |
| 14 | `test_get_books_for_children_true` | Проверка, что метод возвращает только книги без возрастных ограничений.            |
| 15 | `test_get_books_for_children_with_not_accessible_genre_is_empty` | Проверка, что метод возвращает пустой список, если все книги с ограничениями.      |
| 16 | `test_add_book_in_favorites_add_favorite_book_true` | Проверка добавления книги в избранное.                                             |
| 17 | `test_add_book_in_favorites_not_add_favorite_book_is_empty` | Проверка, что книга не попадает в избранное без добавления.                        |
| 18 | `test_add_book_in_favorites_add_favorite_and_not_favorite_books_just_favorite_book` | Проверка, что добавляется в избранное только одна из двух книг.                    |
| 19 | `test_delete_book_from_favorites_delete_correct_book_delete_correct_book` | Проверка успешного удаления книги из избранного.                                   |
| 20 | `test_delete_book_from_favorites_delete_wrong_book_nothing_delete` | Проверка, что попытка удалить несуществующую книгу из избранного ничего не делает. |
