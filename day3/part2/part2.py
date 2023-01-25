import os.path
import pathlib 
import os

def read_data(path):
    data = ""
    with open(path, "r") as f:
        data = f.read()
    return data

def get_data_file_path():
    current_path = pathlib.Path(__file__).parent.parent
    data_file_path = os.path.join(current_path, 'data/data.txt')
    return data_file_path

def get_test_data_file_path():
    current_path = pathlib.Path(__file__).parent.parent
    data_file_path = os.path.join(current_path, 'data/test_data_part1.txt')
    return data_file_path

def process_data(data):
    grand_total = 0

    for n, line in enumerate(data.split("\n")):
        if (n+1%3 == 0):
          old_words = words
          words = []
          words.append(line)
          word1 = words[0]
          word2 = words[1]
          word3 = words[2]
          common_elements = commoon_element
        else:
          words.append(line)

        common_elements = commoon_element(word1, word2)

        print(f"Word1: {word1}, Word2: {word2}, Common Elements: {common_elements}")

        for i in common_elements:
            if is_uppercase(i):
                grand_total += is_uppercase_priority(i)
            elif is_lowercase(i):
                grand_total += is_lowercase_priority(i)

    print(f"The grand total is: {grand_total}")


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
    try:
        if os.environ['TEST'] is not None:
            path = get_test_data_file_path()
    except:
        path = get_data_file_path()

    data = read_data(path)

    process_data(data)