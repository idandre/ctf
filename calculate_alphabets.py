#! /usr/bin/python3

from itertools import chain

count = 0
ret = ''
solList = [0x68, 0x6f, 0x37, 0x57, 0x55, 0x25, 0x3, 0x00, 0x44, 0x00, 0x59, 0x5a, 0x5f, 0x41, 0x3B, 0x39, 0x19, 0x6b, 0x56, 0x1a]

def myXOR(i,j,sol):
  global count
  global ret 
  xor = i^j
  if(xor == sol):
    count+=1
    ret += chr(i)

for s in solList:
  myRange = chain(range(48,58), range(0x5F, 0x60), range(65,91), range(97,123))
  for i in myRange:
    myRange = chain(range(48,58), range(0x5F, 0x60), range(65,91), range(97,123))
    for j in myRange:
      myXOR(i,j,s)
  print(hex(s) + ': ' + ret)
  ret = ''
input()
