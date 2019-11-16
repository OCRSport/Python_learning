# у меня все функции "грязные", поэтому взял несколько функций из вашего примера, сами функции - в leonids_functions.py
import leonids_functions
import functions
import json


def test_author_info():
    assert leonids_functions.author_info() == 'Leonid Orlov'


def test_separator():
    assert leonids_functions.separator(5) == '*****'


def test_is_correct_choice():
    assert leonids_functions.is_correct_choice('6') == True


# грязная функция, не уверен что сработает у кого-то другого
def test_filenames():
    assert leonids_functions.filenames() == ['.gitignore', '111.py', 'account.txt', 'file_maneger.py', 'functions.py', 'leonids_functions.py', 'LICENSE', 'listdir.txt', 'orders.txt', 'README.md', 'test_filemanager.py', 'test_python.py', 'use_functions.py', 'victory.py', 'windows']


# тест новой функции
def test_save_dir():
    with open('listdir.txt', 'r') as f:
        assert functions.save_dir() == dict(json.load(f))
