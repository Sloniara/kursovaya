from file1 import mask_card_number, mask_account_number, reformat_date, print_last_5_executed_operations

def test_mask_card_number_empty_input():
    assert mask_card_number('') == ''

def test_mask_card_number_valid_input():
    assert mask_card_number('1234567890123456') == '**** **** **** 3456'

def test_mask_account_number_empty_input():
    assert mask_account_number('') == ''

def test_mask_account_number_valid_input():
    assert mask_account_number('1234567890') == '**** **** **** 7890'

def test_reformat_date():
    assert reformat_date('2023-01-01T12:00:00') == '01.01.2023'

def test_print_last_5_executed_operations_empty_input(capsys):
    operations_data = []
    print_last_5_executed_operations(operations_data)
    captured = capsys.readouterr()
    assert captured.out == ''

def test_print_last_5_executed_operations_valid_input(capsys):
    operations_data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T12:00:00",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Transaction 1",
            "from": "Card 1234 5678",
            "to": "Account 123456789"
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2023-01-02T12:00:00",
            "operationAmount": {
                "amount": "200.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Transaction 2",
            "from": "Card 9876 5432",
            "to": "Account 987654321"
        }
    ]
    print_last_5_executed_operations(operations_data)
    captured = capsys.readouterr()
    assert captured.out != ''


