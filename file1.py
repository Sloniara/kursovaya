import json
from datetime import datetime
import re


def load_operations(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def mask_card_number(card_number):
    if card_number:
        card_only_number = re.sub(r'\D', '', card_number)
        card_only_name = re.sub(r'\d', '', card_number)
        if len(card_only_number) == 16:
            mask_number = f'{card_only_number[:-12]} {card_only_number[4:-10]}** **** {card_only_number[12:16]}'
        else:
            mask_number = f"**** **** **** **** {card_only_number[16:20]}"
        return f'{card_only_name} {mask_number}'
    else:
        return ''

    #
    # card_only_name = re.sub('\d', '', card_number)
    # print(card_only_name)
def mask_account_number(account_number):
    return f"**** **** **** {account_number[-4:]}" if account_number else ''


def reformat_date(date):
    date = datetime.strptime(date[:10], "%Y-%m-%d")
    return datetime.strftime(date, "%d.%m.%Y")

def print_last_5_executed_operations(operations_data):
    executed_operations = [op for op in operations_data if op.get('state') == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)[:5]

    for op in sorted_operations:
        date = reformat_date(op.get('date'))
        description = op['description']
        source = mask_card_number(op.get('from', ''))
        destination = mask_account_number(op.get('to', ''))
        amount = op['operationAmount']['amount']
        currency = op['operationAmount']['currency']['name']


        print(f"{date} {description}")
        print(f"{source} -> {destination}")
        print(f"{amount} {currency}")
        print()

if __name__ == "__main__":
    operations_data = load_operations('operations.json')
    print_last_5_executed_operations(operations_data)