# people = {
#     'Alice':{
#         'phone':'18800000000',
#         'addr':'Foo drive 23'
#     },
#     'Beth':{
#         'phone':'17700000000',
#         'addr':'Bar street 42'
#     },
#     'Cecil':{
#         'phone':'16600000000',
#         'addr':'Baz avenue 90'
#     }
# }
#
# print (people)
# print (people['Beth'])
# print (people['Beth']['addr'])
#
#
# labels = {
#     'phone':'phonenumber',
#     'addr':'address'
# }
#
# name = input('Name:')
#
# request = input('Phone number (p) or address (a)?')
# if request == 'p':key = 'phone'
# if request == 'a':key = 'addr'
# print (labels[key])
#
# if name in people :print("%s's %s is %s."% (name,labels[key],people[name][key]))


phonebook = {'Alice':'2341','Beth':'5551','Clice':'4444'}
print("Clice's phone number is %(Clice)s." % phonebook)

return_value = phonebook.clear()
print (return_value)


x = {}
y = x
print('x:',x,'y:',y)
x['key'] = 'value'
print('x:',x,'y:',y)
# x = {}
x = x.clear()
print('x:',x,'y:',y)