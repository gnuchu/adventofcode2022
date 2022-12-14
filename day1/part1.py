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


def process_data(data):
  each_elf = data.split("\n\n")
  totals = {}

  for i, cals in enumerate(each_elf):
    total_cals = 0
    elfs_cals = cals.split("\n")
    for j in elfs_cals:
      try:
        total_cals += int(j)
      except ValueError as error:
        pass #Ignore empty last line here.
    
    print(f"Elf {i+1} has {total_cals}")
    totals[i] = total_cals

  sorted_dict = sorted(totals.items(), key = lambda x:x[1])
  print(sorted_dict)

if __name__ == "__main__":
    path = get_data_file_path()
    data = read_data(path)

    process_data(data)