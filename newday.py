#!/usr/bin/env python3
import sys
import os
from pathlib import Path

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

def cargo_new(path, part):
  try:
    os.chdir(path)
  except OSError as error:
    raise OSError(f"{error}")
  
  command = "cargo new part" + str(part)
  print("-------------------")
  print(f"Running command - {command}")
  print("-------------------")
  os.system(command)

def main(): 
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

  cargo_new(path, 1)
  cargo_new(path, 2)
  create_data_folder(path)


if __name__ == "__main__":
  # for i, p in enumerate(sys.argv):
  #   print(f"Param {i} - {p}")
  main()

