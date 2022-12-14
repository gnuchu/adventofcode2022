#!/usr/bin/env python3
import sys
import os
from pathlib import Path
import requests

def get_data(base_url, day):
  url = os.path.join(base_url, str(day), "input")
  token = ""  
  print(f"Getting url - {url}")

  with open('/Users/gnuchu/.config/aocd/token', 'r') as f:
    token = f.read().strip()

  resp = requests.get(url, cookies={"session": token}, allow_redirects=False)
  data = resp.text
  return data

def write_data(data_file, data):
  try:
    with open(data_file, "w") as f:
      f.write(data)
  except OSError as error:
    raise OSError(f"{error}")
  

def create_data_folder(path):
  try:
    os.chdir(path)
  except OSError as error:
    raise OSError(f"{error}")
  
  p = os.path.join(path, 'data')
  try:
    os.mkdir(p)
  except OSError as error:
    raise OSError(f"{error}")
  
  try:
    os.chdir(p)
  except OSError as error:
    raise OSError(f"{error}")
  
  data_file = os.path.join(p, 'data.txt')
  Path(data_file).touch()
  return data_file

def cargo_new(path, part):
  try:
    os.chdir(path)
  except OSError as error:
    raise OSError(f"{error}")
  
  command = "cargo new part" + str(part)
  os.system(command)

def create_path():
  day_number = 0
  path_base = '/Users/gnuchu/projects/adventofcode2022'

  if len(sys.argv) < 2:
    raise ValueError("Pass in day number")

  try: 
    day_number = int(sys.argv[1])
  except:
    raise ValueError("Can't convert passed day number to int")

  folder = "day" + str(day_number)
  path = path_base + '/' + folder
  if os.path.exists(folder):
    raise IsADirectoryError("Already exists")
  
  try:
    os.mkdir(path)
  except OSError as error:
    raise OSError(f"{error}")

  return path

def main():
  base_url = "https://adventofcode.com/2022/day/"
  path = create_path()
  day = sys.argv[1]
  cargo_new(path, 1)
  cargo_new(path, 2)
  data_file = create_data_folder(path)
  data = get_data(base_url, day)
  write_data(data_file, data);


if __name__ == "__main__":
  # for i, p in enumerate(sys.argv):
  #   print(f"Param {i} - {p}")
  main()

