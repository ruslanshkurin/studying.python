'''
@author: Ruslan
'''
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print D
D['food']='Apple'
D['quantity']+=1
print D
print D['food']

D = {}
D['Name'] = 'Ruslan'
D['Job'] = 'Dev'
D['Age'] = 25
print D

print '=====Nesting======='
person = {'Name': {'First': 'Ruslan', 'Second': 'Shkurin'},
          'Job': ['Prgrammer', 'Architect'],
          'Age': 25}
print person['Name']["First"]
print person['Job'][-1]
person['Job'].append('Manager')
print person
D[1] = 'Helllo'
print D

print '===== Sorting by keys, for cicle ==========='
print sorted(D)
for key in sorted(D):
    print str(key)+' is '+str(D[key])

print '========= While Cicle ==================='
x = 4
while x > 0:
    print('spam!' * x)
    x -= 1