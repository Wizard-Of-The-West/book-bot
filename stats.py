from collections import Counter


def get_num_words(string: str) -> int:
    return len(string.split())


def count_characters(string: str) -> dict:
    string_to_count = string.lower()
    return Counter(string_to_count)


def character_report(char_dict: dict) -> list:
    report_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            letter_dict = {"char": key, "num": value}
            report_list.append(letter_dict)

    return sorted(report_list, key=lambda x: x["num"], reverse=True)
