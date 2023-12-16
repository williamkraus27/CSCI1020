import argparse
from random import random, choice, randrange
def LCS_dp(DNA1=None, DNA2=None): 
  nucleotides = ['A', 'C', 'T', 'G']  
  d1 = ''                             
  d2 = ''
  empty = randrange(1,13)           
  if DNA1 is None:                    
    for _ in range(empty):            
      d1 = d1 + choice(nucleotides)
      d2 = d2 + choice(nucleotides)
    DNA1 = d1
    DNA2 = d2
    print(DNA1, DNA2)
  if DNA2 is None:                    
    for _ in range(DNA1):            
      d1 = d1 + choice(nucleotides)
      d2 = d2 + choice(nucleotides)
    DNA1 = d1
    DNA2 = d2
    print(d1, d2)
    
  rows = len(DNA1) + 1                      
  columns = len(DNA2) + 1
  dp = [[0]*columns for _ in range(rows)]  
  i = 1
  j = 1
  
  while i <= len(DNA1) and j <= len(DNA2): 
    if DNA1[i-1] == DNA2[j-1]:             
      dp[i][j] = dp[i-1][j-1] +1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])  
    j += 1
    if j == len(DNA1) + 1:                   
      i += 1
      j = 1
  print('Intermediate table of values:')
  for row in dp:
    print(row)

  y = len(DNA1)
  z = len(DNA2)
  subsequence = ""
  while y > 0 and z > 0:                       
    current_cell = dp[y][z]
    left_cell = dp[y][z-1]
    top_cell = dp[y-1][z]
    diag_cell = dp[y-1][z-1]
    if current_cell == (diag_cell + 1) and DNA1[y-1] == DNA2[z-1]:   
      subsequence = subsequence + DNA2[z-1]
      y -= 1
      z -= 1
    elif current_cell == (diag_cell + 1) and DNA1[y-1] != DNA2[z-1]:  
      if left_cell == top_cell:
        y -= 1
      elif left_cell < top_cell:
        y -= 1
      elif left_cell > top_cell:
        z -= 1
    elif current_cell == diag_cell:
      y -= 1
  subsequence_new = subsequence[::-1]                                 
  return ('The longest common subsequence is', subsequence_new, 'with a length of', len(subsequence))

def main():
  parser=argparse.ArgumentParser(description='Find the longest common subsequence. Enter an integer beween 1 and 12, two strings, or no argument.')

  parser.add_argument("--number", type=int, help='Enter a number between 1 and 12')
  parser.add_argument("--string1", type=str, help='Enter your first sequence')
  parser.add_argument("--string2", type=str, help='Enter your second sequence')

  args=parser.parse_args()

  if args.string1 and args.string2:
    result = LCS_dp(args.string1, args.string2)
  elif args.number:
    result = LCS_dp(args.number)
  else:
    result = LCS_dp()
  
  print(result) 

if __name__ == '__main__':
  main()
 









