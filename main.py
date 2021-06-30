import random

def play():
    user = input("Pick your poison! 'r' for Rock, 'p' for Paper, or 's' Scissors?")

    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
      return "You and the computer have both chosen {}. So you tied.".format(computer)

    if is_win(user, computer):
      return "You chose {} and the computer chose {}. You won!".format(user, computer)
      
    return "{} loses to {}... womp womp".format(user, computer)
  
def is_win(player, opponent):
  if ( player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
      return True
  return False


if __name__ == '__main__':
    print(play())
