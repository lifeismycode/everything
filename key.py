# Welcome to the random key library
# There is one function that is random
# The argument of the function is the length of the key that will result

from random import randrange
import error

def random(length):
  if length < 1:
    error.error('Invalid length')
  
  sn = []
  sl = ''
  
  de = length
  
  def defapp(a, b):
    si = ord(a)
    se = si + b
    while si < se:
      if len(chr(si)) == 1:
        sn.append(chr(si))
        si = si + 1
  defapp('a', 26)
  defapp('A', 26)
  defapp('0', 10)
  
  al = 0
  while (al < int(de)):
    sl = sl + sn[randrange(0, 61)]
    al = al + 1
  
  return sl
