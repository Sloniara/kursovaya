import json
import pytest
from datetime import datetime
from file1 import load_operations, mask_card_number, mask_account_number, reformat_date, print_last_5_executed_operations

# Подготовка тестовых данных
sample_operations_data = [
    {
        "state": "EXECUTED",
        "date": "2022-01-01T12:34:56",
        "description": "Purchase",
        "from": "1234 5678 9012 3456",
        "to": "9876543210",
        "operationAmount": {"amount": 100, "currency": {"name": "USD"}},
    },
    # Добавьте еще тестовых данных при необходимости
]

def test_load_operations(tmpdir):
    # Создаем временный файл с тестовыми данными
    operations_file = tmpdir.join("operations.json")
    operations_file.write(json.dumps(sample_operations_data))

    # Загружаем операции из временного файла
    operations_data = load_operations(str(operations_file))

    # Проверяем, что данные были успешно загружены
    assert operations_data == sample_operations_data


def test_mask_account_number():
    assert mask_account_number("1234567890") == "**** **** **** 7890"
    assert mask_account_number("") == ""

def test_reformat_date():
    assert reformat_date("2022-01-01T12:34:56") == "01.01.2022"

def test_load_operations_invalid_file():
    # Проверка поведения при попытке загрузить данные из несуществующего файла
    with pytest.raises(FileNotFoundError):
        load_operations("invalid_file.json")

def test_mask_card_number_invalid_input():
    # Проверка поведения при передаче невалидного номера карты (не строка)
    with pytest.raises(TypeError):
        mask_card_number(1234567890123456)

def test_mask_account_number_invalid_input():
    # Проверка поведения при передаче невалидного номера счета (не строка)
    with pytest.raises(TypeError):
        mask_account_number(1234567890)
def test_print_last_5_executed_operations_empty_data(capsys):
    # Проверка поведения при передаче пустого списка операций
    print_last_5_executed_operations([])
    captured = capsys.readouterr()
    assert captured.out == ""

def test_print_last_5_executed_operations_no_executed_operations(capsys):
    # Проверка вывода при отсутствии выполненных операций
    operations_data = [{"state": "PENDING"}] * 5  # Создаем список из 5 операций со статусом PENDING
    print_last_5_executed_operations(operations_data)
    captured = capsys.readouterr()
    assert captured.out == ""





