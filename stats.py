def get_sorted_value(dict):
    list = []
    for key in dict:
        list.append({ "char": key, "count": dict[key] })

    print(list)
    def sort_function(value):
        return value["count"]

    list.sort(reverse=True, key=sort_function)
    return list


def get_words_count(text):
    return len(text.split())

def get_letter_count(text):
    dict = {}
    for c in text:
        char = c.lower()
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict
