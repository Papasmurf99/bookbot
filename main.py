def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_count = count_words(text)
    chars_dict = char_count(text)
    chars_sorted = print_formatted_char_count(chars_dict)

    print(f'--- Begin report on {book_path} ---')
    print(f'Word count: {word_count}')
    print_formatted_char_count(chars_dict)
    
    
    

def char_count(text):
    char_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_on(char_dict):
    return char_dict['count']

def convert_to_list_of_dicts(char_dict):
    return [{'char': char, 'count': count} for char, count in char_dict.items()]

def print_formatted_char_count(char_dict):
    char_list = convert_to_list_of_dicts(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    for item in char_list:
        print(f"The {item['char']} chacter was found {item['count']} times.") 

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
     words = text.split()
     return len(words)       
main()            