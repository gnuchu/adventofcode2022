import os.path
import pathlib 
from game import Game
import os
import sys

def read_data(path):
  data = ""
  with open(path, "r") as f:
    data = f.read()
  return data

def get_data_file_path():
  current_path = pathlib.Path(__file__).parent
  data_file_path = ""
  try:
    if os.environ['TEST_DATA'] == '1':
      data_file_path = os.path.join(current_path, 'data/test_data.txt')
  except:
    data_file_path = os.path.join(current_path, 'data/data.txt')
  
  return data_file_path

def score_for_play(play):
  # 1 for Rock(A,X), 2 for paper(B,Y), 3 for scissors(C,Z)
  if play in ["X", "A"]:
    return 1
  elif play in ["Y", "B"]:
    return 2
  elif play in ["Z", "C"]:
    return 3

def score_for_game(result, player):
  if player == "me":
    if result == "elf":
      return 0
    elif result == "draw":
      return 3
    elif result == "me":
      return 6
  elif player == "elf":
    if result == "elf":
      return 6
    elif result == "draw":
      return 3
    elif result == "me":
      return 0

def total_score(play, result, player):
  return score_for_play(play) + score_for_game(result, player)

def process_data(data):
  lines = data.split("\n")
  my_score = 0

  for i, line in enumerate(lines):
    try:
      (elf, me) = line.split(' ')
      game = Game(elf, me)
      result = game.winner()
      
      s = total_score(me, result, "me")

      print(f"{str(i)}: " + result + f" [{s}]")

      my_score += s
      
    except:
      raise

  print(f"Total Score:" + f" [{my_score}]")

if __name__ == "__main__":
    path = get_data_file_path()
    data = read_data(path)

    process_data(data)