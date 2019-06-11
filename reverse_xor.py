#! /usr/bin/python3

def get_char(number, i):
  return chr(int.to_bytes(number, 8, 'big')[i])

def print_table(xor, c1, n1, c2, n2):
  print('chr(' + c1 + ') :', ' ', ' ', ' ', ' ',get_char(n1, 4), get_char(n1, 5), get_char(n1, 6), get_char(n1, 7))
  print(c1 + '      :', hex(n1)[2:])
  print(c2 + '      :', hex(n2)[2:])
  print(c1 + '^' + c2 + '    :', hex(xor)[2:], '\n')

c_xor_d = 0x196b561a6b335f66 #copy out of cutter && reverse
d = 0xffffffff00000000
c = d ^ c_xor_d

b_xor_c = 0x4400595a5f413b39
b = c ^ b_xor_c

a_xor_b = 0x686f375755250300
a = b ^ a_xor_b

print_table(a_xor_b, 'a', a, 'b', b)
print_table(b_xor_c, 'b', b, 'c', c)
print_table(c_xor_d, 'c', c, 'd', d)
input()
