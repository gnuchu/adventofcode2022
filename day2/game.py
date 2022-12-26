class Game():
  elf = ""
  me = ""
  
  def sanitise_input(self, input, player):
    try:
      if input.upper() not in ["A", "B", "C", "X", "Y", "Z"]:
        raise ValueError
      
      if player == 1:
        if input.upper() not in ["A", "B", "C"]:
          raise ValueError
      elif player == 2:
        if input.upper() not in ["X", "Y", "Z"]:
          raise ValueError

      return input

    except ValueError as error:
      return ValueError
    

  def __init__(self, elf, me):
    p1 = self.sanitise_input(elf, 1)
    p2 = self.sanitise_input(me, 2)
    self.elf = p1.upper()
    self.me = p2.upper()
  
  def winner(self):
    score = 0
    win = self.winning_hand(self.elf, self.me)
    if win == 0:
      return "draw"
    elif win == 1:
      return "elf"
    elif win == 2:
      return "me"
      
  # rock, paper, scissors
  # AX, BY, CZ

  # paper(B,Y) beats rock (A,X)
  # rock(A,X) beats scissors (C,Z)
  # scissors(C,Z) beats paper (B,Y]

  # [A, X] loses to [B, Y]
  # [C, Z] loses to [A, X]
  # [B, Y] loses to [C, Z]

  def winning_hand(self, hand1, hand2):
    print(f"Hand1 = {hand1}, Hand2 = {hand2}")
    if hand1 in ["A", "X"]: #Rock
      if hand2 in ["A", "X"]: #Rock
        return 0
      elif hand2 in ["B", "Y"]: #Paper
        return 2
      elif hand2 in ["C", "Z"]: #Scisosors
        return 1

    elif hand1 in ["B", "Y"]: #Paper
      if hand2 in ["A", "X"]: #Rock
        return 1
      elif hand2 in ["B", "Y"]: #Paper
        return 0
      elif hand2 in ["C", "Z"]: #Scissors
        return 2

    elif hand1 in ["C", "Z"]: #Scissors
      if hand2 in ["A", "X"]: #Rock
        return 2
      elif hand2 in ["B", "Y"]: #Paper
        return 1
      elif hand2 in ["C", "Z"]: #Scissors
        return 0


