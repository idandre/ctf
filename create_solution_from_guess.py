#! /usr/bin/python3

import sys

guess = sys.argv[1] + 'aWg_'

print(sys.argv[1], len(sys.argv[1]))
print(guess, len(guess))
a_xor_b = 0x686f375755250300
b_xor_c = 0x4400595a5f413b39
c_xor_d = 0x196b561a6b335f66

def get_char(number, i):
  return chr(int.to_bytes(number, 8, 'big')[i])

def print_table(xor, c1, n1, c2, n2):
  print('chr(' + c1 + ') :', get_char(n1, 0), get_char(n1, 1), get_char(n1, 2), get_char(n1, 3) ,get_char(n1, 4), get_char(n1, 5), get_char(n1, 6), get_char(n1, 7))
  print(c1 + '      :', hex(n1)[2:])
  print(c2 + '      :', hex(n2)[2:])
  print(c1 + '^' + c2 + '    :', hex(xor)[2:], '\n')

def print_tables(my_string):
  a = int.from_bytes(str.encode(my_string, 'ascii'), 'big')

  b = a ^ a_xor_b
  c = b ^ b_xor_c
  d = c ^ c_xor_d

  print_table(a_xor_b, 'a', a, 'b', b)
  print_table(b_xor_c, 'b', b, 'c', c)
  print_table(c_xor_d, 'c', c, 'd', d)
  print_table(0, 'd', d, '0', 0)

print_tables(guess)


input()
