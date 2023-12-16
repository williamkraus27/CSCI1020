import argparse
from random import random, choice, randrange
def LCS_re(seq1=None, seq2=None, i=None, j=None):
  ascii = [65, 67, 71, 84]
  empty = randrange(1,13)
  s1 = ''
  s2 = ''
  if seq1 is None:    
    for _ in range(empty):
      s1 = s1 + (chr(choice(ascii)))
    for _ in range(empty):
      s2 = s2 + (chr(choice(ascii)))
  if seq2 is None:
    if isinstance(seq1, int):
      for _ in range(seq1):
        s1 = s1 + (chr(choice(ascii)))
      for _ in range(seq1):
        s2 = s2 + (chr(choice(ascii)))
    seq1 = s1
    seq2 = s2
    print(s1, s2)
  if i is None:
    i = len(seq1)
  if j is None:
    j = len(seq2)
  if i == 0 or j == 0:
    return 0
  elif seq1[i-1] == seq2[j-1]:
    return 1 + LCS_re(seq1, seq2, i-1, j-1)
  else:
    return max((LCS_re(seq1, seq2, i-1, j)), (LCS_re(seq1, seq2, i, j-1)))
    



def main():
  parser = argparse.ArgumentParser(description='Find the longest common subsequence. Enter an integer beween 1 and 12, two strings, or no argument.')
  parser.add_argument("--number", type=int, help='Enter a number between 1 and 12')
  parser.add_argument("--string1", type=str, help='Enter your first sequence')
  parser.add_argument("--string2", type=str, help='Enter your second sequence')

  args = parser.parse_args()

  if args.string1 and args.string2:
    result = LCS_re(args.string1, args.string2)
  elif args.number:
    result = LCS_re(args.number)
  else:
    result = LCS_re()


  print(result) 

if __name__ == '__main__':
  main()
 