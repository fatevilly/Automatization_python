import pytest
from string_utils import StringUtils

utils = StringUtils()

#1
@pytest.mark.parametrize("input_string, expected_output", [
    ("frank", "Frank"),
    ("добрый день", "Добрый день"),
    ("120824", "120824"),
    ("", ""),
    ("  ", "  "),
    ("12august", "12august")
    ])

def test_capitilize(input_string, expected_output):
    assert utils.capitilize(input_string) == (expected_output)

#2
def test_trim():
    #POSITIVE
    assert utils.trim(" skypro") == "skypro"
    assert utils.trim("  привет") == "привет"
    assert utils.trim("  August  ") == "August  "
    #NEGATIVE
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(123456) == "123456"

@pytest.mark.xfail()
def test_trim_with_with_space_output():
    assert utils.trim("  August  ") == "  AUGUST  "

#3
@pytest.mark.parametrize("string, delimeter, result", [
   #POSITIVE
   ("мяч,скакалка,обруч", ",", ["мяч", "скакалка", "обруч"]),
   ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
   ("&@^@*@$", "@", ["&", "^", "*", "$"]),
   #NEGATIVE
   ("", None, []),
   ("1,2,3,4 5", None, ["1", "2", "3", "4 5"])
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result

#4
@pytest.mark.parametrize("string, symbol, result", [
    ("книга", "к", True),
    ("  береза", "з", True),
    ("лес  ", "с", True),
    ("finish", "i", True),
    ("Баба-яга", "-", True),
    ("2024", "4", True),
    ("", "", True),
    ("Челябинск", "ч", False),
    ("город", "я", False),
    ("крюк", "№", False),
    ("", "e", False),
    ("54321", "r", False)
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result 

#5
@pytest.mark.parametrize("string, symbol, result", [
    ("квартира", "к", "вартира"),
    ("ветер", "т", "веер"),
    ("Иван", "И", "ван"),
    ("54321", "5", "4321"),
    ("автор песни", " ", "авторпесни"),

    ("", "", ""),
    ("Андрей", "з", "Андрей"),
    ("", "у", ""),
    ("цветы", "", "цветы"),
    ("звезда ", " ", "звезда")
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

#6
@pytest.mark.parametrize("string, symbol, result", [
    ("книга", "к", True),
    ("Березники", "Б", True),
    ("54321", "5", True),
    ("Super", "S", True),
    ("Санкт-Петербург", "С", True),
    ("", "", True),
    
    ("Челябинск", "ч", False),
    ("город", "Г", False),
    ("крюк", "№", False),
    ("", "e", False),
    ("54321", "r", False)
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

#6
@pytest.mark.parametrize("string, symbol, result", [
    ("runs", "s", True),
    ("Краски", "и", True),
    ("54321", "1", True),
    ("SUPER", "R", True),
    ("пейзаж ", "", True),
    ("", "", True),
    ("Чудо-юдо", "о", True),
    
    ("стихотворение", "с", False),
    ("проза", "А", False),
    ("роман", "№", False),
    ("", "%", False),
    ("54321", "r", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

#7
@pytest.mark.parametrize("string, result", [
    ("", True),
    (" ", True),
    ("  ", True),
    ("слово", False),
    ("много слов", False),
    ("54321", False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

#8
@pytest.mark.parametrize("lst, joiner, result", [
    (["g", "o", "o", "d"], ",", "g,o,o,d"),
    ([1, 2, 3], None, "1, 2, 3"),
    (["Слово", "Заслово"], "-", "Слово-Заслово"),
    (["Слово", "Заслово"], "между", "СловомеждуЗаслово"),
    (["С", "С", "С", "Р"], "", "СССР"),

    ([], None, ""),
    ([], ",", ""),
    ([], "привет", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
        assert res == result








