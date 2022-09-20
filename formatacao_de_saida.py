n = 101

print('%d (decimal) in octal is %o and in hexa is %x' % (n,n,n))

idade = 20
nome = 'Moises'
string = 'meu nome é {}, eu tenho {} anos'

print(string.format(nome, idade))

print('{0} (decimal) in octal is {0:o} and in hexa is {0:x}'.format(n))

print('-----------------------------------------')
print("%20s %15s %2s" % ('Email', 'Name', 'Sex'))
# data line 1
print("%20s %15s %2s" % ('davi@pf.com', 'David Gilmour', 'M'))
# data line 2
print("%20s %15s %2s" % ('nickmason@domain.com', 'Nick Mason', 'M'))
# data line 3
print("%20s %15s %2s" % ('richard@dot.com', 'Richard Wright', 'M'))
print('-----------------------------------------')

print("{:d} {:03d} {:>6d}".format(123, 17, 932))

# floats
print("{0:f} {0:>4.1f} {0:06.2f}".format(1.13))

