import math
class Solution:
   def reverse(self, x: int) -> int:
      numstr = str(x)
      if numstr[0] == '-':
         isneg = True
      else:
         isneg = False
      listnum = list(enumerate(numstr))
      listnum.sort(reversed=True)
      numstr.rs
