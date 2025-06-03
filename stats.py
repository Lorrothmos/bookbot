def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def wordcount(count_text):
    text_set = count_text.split()
    words = len(text_set)
    return words

def sort_on(dict):
    return dict["count"]

def create_list(dict):
    dict_list = []
    for letter in dict:
        temp_dict = {"letter": f"{letter}", "count": dict[letter]}
        dict_list.append(temp_dict)
        dict_list.sort(reverse=True, key=sort_on)
    return(dict_list)


def character_count(the_text):
    dictionary = {}
    lowercase_text = the_text.lower()
    for character in lowercase_text:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] =1
    return dictionary
