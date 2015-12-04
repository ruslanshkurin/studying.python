'''
@author: Ruslan
'''
# Lists are sequances
from __builtin__ import str

print '=============Lists==========='
a = [1232, 'qwerty', 7.8]
print a

print a[1]
print a[-1]
print a[:-1]
print a + ['Hello', 'World']

print '\nLists specific methods'
a.append('!')
print a
print a.pop(2)
print a
a.sort()
print a

print '\nNested Lists'
nested = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print nested
print nested[2][0]

print '''list comprehension 
        expressions'''
col2 = [row[1] for row in nested]
print col2
print [row[1] for row in nested if row[1] % 2 == 0]
print 'matrix diag: ' + str([nested[i][i] for i in [0, 1, 2]])
