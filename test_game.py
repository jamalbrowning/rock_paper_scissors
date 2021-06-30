import unittest
from unittest import result
import main


class TestPlay(unittest.TestCase):
    '''
    Rock = r , Paper = p , Scissors = s
    Test for combinations
    r/r , r/p , r/s
    s/s , s/p , s/s
    p/p , p/s, p/r
    '''  


    def test_play_tie_rock(self):
      result = main.is_win('r', 'r')
      self.assertEqual(result, False)

    def test_play_tie_scissors(self):
      result = main.is_win('s', 's')
      self.assertEqual(result, False)

    def test_play_tie_paper(self):
      result = main.is_win('p', 'p')
      self.assertEqual(result, False)   

    def test_play_win_rock_scissors(self):
      result = main.is_win('r', 's')
      self.assertEqual(result, True)

    def test_play_win_rock_paper(self):
      result = main.is_win('r', 'p')
      self.assertEqual(result, False)

    def test_play_win_paper_scissors(self):
      result = main.is_win('p', 's')
      self.assertEqual(result, False) 

    def test_play_win_paper_rock(self):
      result = main.is_win('p', 'r')
      self.assertEqual(result, True)  

    def test_play_win_scissors_paper(self):
      result = main.is_win('s', 'p')
      self.assertEqual(result, True)

    def test_play_win_scissors_rock(self):
      result = main.is_win('s', 'r')
      self.assertEqual(result, False)   


if __name__ == '__main__':
  unittest.main()
