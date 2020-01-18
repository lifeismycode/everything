# Welcome to the simple Yaniv cool Python encryption library
# stringEncryption is the function of text encoding within this directory
# stringDecryption is the function of text decoding within this directory

import error

def stringEncryption(string, key):
  if string == '':
    error.error('A key cannot be empty')
  elif key == '':
    error.error('A key cannot be empty')
  s = ''
  z = 0
  for i in string:
    e = 0
    q = 0
    for a in key:
      q = q + ord(a)
    e = e + ord(i) * q * len(string) * (z + 1)
    s = s + str(chr(e))
    if z < len(string) - 1:
      s = s + ';'
    z = z + 1
  return s

def stringDecryption(string, key):
  try:
    if string == '':
      error.error('A key cannot be empty')
    elif key == '':
      error.error('A key cannot be empty')
    e = ''
    s = str(string).split(';')
    d = 0
    for i in s:
      w = int(ord(i))
      g = []
      for a in key:
        g.insert(0, a)
      q = 0
      for p in g:
        q = q + ord(p)
      w = w / len(s) / q / (d + 1)
      e = e + chr(int(w))
      d = d + 1
    return e
  except Exception:
    error.error('Incorrect key or string')
