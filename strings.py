'''
@author: Ruslan
'''
print 'Strings are Sequences!'
s = 'Hello World'
print len(s)
print s[0]
print s[1]
print s[-1] # equal to print s[len(s) - 1]
print s[len(s) - 1]

print "\n====Slicing===="
print s[1:4]
print s[:4]
print s[1:]
print s[:-2]
print s[:]

print "\n====Concat===="
print s + '!'
print s * 3

print "\n====Strings are immutable===="
#s[0] = 'u'
 
print '\nString specific functions'
print s.find('llo')
print s.replace('World', 'Bitch!')
print s.split(' ')
print s.upper()

print '\nString formatting'
print '%s, eggs, and %s' % ('spam', 'SPAM!')
print '{0}, eggs, and {1}'.format('spam;', 'SPAM!') # from Python 2.6

print '\n|all methods and attribute of object|'
print dir(s)
print '\n|Documentation|'
print help(s.replace)

print '\n|Multiline strings|\n'
msg = '''Putin Huilo
lalala'''
print msg

