def get_word_count(text):
    words = text.split()
    return len(words)

def count_char(text):
    letter_count = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in letter_count:
            letter_count[lowercase_char] += 1
        else:
            letter_count[lowercase_char] = 1
    return letter_count

def sort_letters(letter_dict):
    sorted = []
    for char, count in letter_dict.items():
        if char.isalpha():
            char_info = {"char": char, "num": count}
            sorted.append(char_info)
    sorted.sort(key=lambda item: item["num"], reverse=True)
    return sorted