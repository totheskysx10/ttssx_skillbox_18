import re

phone_numbers = ['9999999999', '999999-999', '99999x9999']


def check_numbers(phone_list):
    for i in range(len(phone_list)):
        result = re.search(r'\b[89]\d{9}\b', phone_numbers[i])
        if result is None:
            print(f"{i + 1} номер: не подходит")
        else:
            print(f"{i + 1} номер: всё в порядке")


check_numbers(phone_numbers)