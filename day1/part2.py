import os.path
import pathlib 

def read_data(path):
  data = ""
  with open(path, "r") as f:
    data = f.read()
  return data

def get_data_file_path():
  current_path = pathlib.Path(__file__).parent
  data_file_path = os.path.join(current_path, 'data/data.txt')
  return data_file_path

if __name__ == "__main__":
    path = get_data_file_path()
    data = read_data(path)

    print(data)