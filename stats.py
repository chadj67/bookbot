def get_num_words(book_text):
   return len(book_text.split())


def get_num_letters(book_text):
    letter_dict = {}
    for letter in book_text.lower():
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict


def sort_on(d):
    return d["num"]


def sort_dict(num_chars_dict):
    dict_as_list = []
    for key in num_chars_dict:
        dict_as_list.append({"char": key, "num": num_chars_dict[key]})
    dict_as_list.sort(key=sort_on,  reverse=True)
    return dict_as_list

