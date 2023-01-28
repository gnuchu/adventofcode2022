#!/usr/bin/env python3
import sys
import os
from pathlib import Path
import requests
import shutil
import pathlib

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
  

def create_data_folder(day_path):
  try:
    os.chdir(day_path)
  except OSError as error:
    raise OSError(f"{error}")
  
  p = os.path.join(day_path, 'data')
  try:
    os.mkdir(p)
    test_data_path = os.path.join(p, 'test_data_part1.txt')
    pathlib.Path(test_data_path).touch()
    test_data_path = os.path.join(p, 'test_data_part2.txt')
    pathlib.Path(test_data_path).touch()
  except OSError as error:
    raise OSError(f"{error}")
  
  try:
    os.chdir(p)
  except OSError as error:
    raise OSError(f"{error}")
  
  data_file = os.path.join(p, 'data.txt')
  Path(data_file).touch()
  return data_file

def python_new(day_apth, base_path):
  try:
    os.chdir(day_apth)
  except OSError as error:
    raise OSError(f"{error}")
  
  parts = ['1', '2']
  template = os.path.join(base_path, 'template/template.py')

  try:
    for part in parts:
      name = 'part' + part
      os.mkdir(name)   
      filename = f"{name}/{name}" + ".py"
      shutil.copy(template, filename)
  except OSError as error:
    raise OSError(f"{error}")
  
def create_path(day_number, base_path):

  folder = "day" + str(day_number)
  folder_path = os.path.join(base_path, folder)

  if os.path.exists(folder_path):
    raise IsADirectoryError("Already exists")
  
  try:
    os.mkdir(folder_path)
  except OSError as error:
    raise OSError(f"{error}")

  return folder_path

def main():
  base_url = "https://adventofcode.com/2022/day/"
  base_path = pathlib.Path().cwd()
  
  if len(sys.argv) < 2:
    raise("Please supply day number as an argument")

  day = sys.argv[1]
  day_path = create_path(day_number=day, base_path=base_path)

  python_new(day_path, base_path)
  
  data_file = create_data_folder(day_path)
  data = get_data(base_url, day)
  write_data(data_file, data);


if __name__ == "__main__":
  # for i, p in enumerate(sys.argv):
  #   print(f"Param {i} - {p}")
  main()