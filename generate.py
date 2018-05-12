from random import choice

def genDNA(length, alph):
   # randomly generates DNA-like sequence
   DNA=""
   for count in range(length):
      DNA+=choice(alph)
   return DNA
