#!/usr/bin/env python3
import sys
import os
import shutil

def cargo_new(path, part):
  part_dir = path + '/' + 'part' + str(part)

  try:
    os.chdir(part_dir)
  except OSError as error:
    raise OSError(f"{error}")
  
  command = "cargo new part" + str(part)
  print("--------------------")
  print(f"Running command - {command}")
  print("--------------------")
  os.system(command)

def main(): 
  template = './template'
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
  
  source = path_base + '/' + template

  try:
    shutil.copytree(source, path)
  except OSError as error:
    raise OSError(f"{error}")

  cargo_new(path, 1)
  cargo_new(path, 2)


if __name__ == "__main__":
  # for i, p in enumerate(sys.argv):
  #   print(f"Param {i} - {p}")
  main()

