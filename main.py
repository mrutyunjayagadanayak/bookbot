def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string_value):
    words = string_value.split()
    return len(words)

def count_character(text):
    character_count = {}
    for char in text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


def sort_on(dict_list):
    return dict_list["count"]

def dict_to_dictlist(dict):
    new_list = []
    for key in dict:
        new_list.append({"char":key,"count":dict[key]})
    new_list.sort(reverse=True,key=sort_on)
    return new_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = remove_non_alphabet(count_character(text))
    character_list = dict_to_dictlist(character_count)
    character_list.sort(reverse=True,key=sort_on)
    print_report(character_list,word_count,book_path)



def remove_non_alphabet(dict):
    new_dict = {}
    for key in dict:
        if key.isalpha():
            new_dict[key] = dict[key]
    return new_dict

def print_report(dict,word_count,path):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()
    for i in dict:
        print(f"The '{i["char"]}' character was found {i["count"]} times")
    
    print("--- End report ---")
main()
    