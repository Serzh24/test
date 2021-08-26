from yandex import YandexDisc

class TestYandexDisc:
    def setup(self):
        print('setup')

    # папка создана успешно
    def test_creating_folder(self):
        assert 201 == YandexDisc().create_folder('folder_name')

    # создание папки возможно
    def test_creating_existing_folder(self):
        assert 409 != YandexDisc().create_folder('folder_name')

    # проверка успешного создания папки через запрос списка файлов
    def test_is_folder_created(self):
        assert 200 == YandexDisc().check_created_folder('folder_name')

    # объект не найден на YandexDisc
    def test_check_miss_folder(self):
        assert 404 == YandexDisc().check_created_folder('folder_name')

    def teardown(self):
        print('teardown')