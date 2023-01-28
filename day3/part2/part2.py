import os.path
import pathlib 
import os
import sys

def read_data(path):
    data = ""
    with open(path, "r") as f:
        data = f.read()
    return data

def get_data_file_path():
    current_path = pathlib.Path(__file__).parent.parent
    data_file_path = os.path.join(current_path, 'data/data.txt')
    return data_file_path

def get_test_data_file_path(part):
    current_path = pathlib.Path(__file__).parent.parent
    data_file_path = os.path.join(current_path, f"data/test_data_part{part}.txt")
    return data_file_path

def process_old_words(old_words):
    # old_word [] of three words that will have one common badge between them.
    
    badge = common_elements(old_words[0], old_words[1], old_words[2])[0]
    if is_lowercase(badge):
        return is_lowercase_priority(badge)
    else:
        return is_uppercase_priority(badge)

def process_data(data):
    words = []
    total = 0
    old_words = []

    for n, line in enumerate(data.split("\n")):
        no = n+1
        if (no%3 == 0):
            words.append(line)
            old_words = words
            total += process_old_words(old_words)
            words = []
        else:
            words.append(line)
    
    print(f"Total = {total}")

def is_lowercase_priority(character):
    return int(ord(character) - 96)

def is_uppercase_priority(character):
    return int(ord(character) - 38)

def is_uppercase(character):
    try:
        if ord(character) > 64 and ord(character) < 91:
            return True
        else:
            return False
    except Exception as e:
        raise(e)

def is_lowercase(character):
    try:
        if ord(character) > 96 and ord(character) < 123:
            return True
        else:
            return False
    except Exception as e:
        raise(e)

def common_elements(str1, str2, str3):
    return list(set(list(str1)) & set(list(str2)) & set(list(str3)))


if __name__ == "__main__":
    part = 2
    try:
        if os.environ['TEST'] is not None:
            path = get_test_data_file_path(part=part)
    except:
        path = get_data_file_path()

    data = read_data(path)

    process_data(data)