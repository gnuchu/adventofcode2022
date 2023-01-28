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

def get_test_data_file_path(part):
    current_path = pathlib.Path(__file__).parent.parent
    data_file_path = os.path.join(current_path, f"data/test_data_part{part}.txt")
    return data_file_path

def process_data(data):
  pass

if __name__ == "__main__":
  part = FAIL_TO_COMPILE_IF_NOT_ENTERED
  
  try:
      if os.environ['TEST'] is not None:
          path = get_test_data_file_path()
  except:
      path = get_data_file_path()

  data = read_data(path)

  process_data(data)