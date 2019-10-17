# print ('%s plus %s equals %s' %(1,1,2))
# # print '%s plus %s equals %s' % 1,1,2

# print ('Price of eggs: $%d' % 42)
# print ('Hexadecimal price of eggs : %x' % 42)


# from math import pi
# print ('Pi:%f...' % pi)
# print('Very inexact estimate of pi: %i'% pi)
# print ('Using str: %s' % '42L')
# print ('Using repr:%r' % '42L')

# print ('%10f' % pi)
# print ('%10.4f' % pi)
# print ('%.4f' % pi)
# print ('%10.5s' % 'Hello World')
# print ('%*.*s' % (10,5,'Hello World'))
# print ('%010.4f' % pi)
# print ('% 10d' % +10)
# print ('% 10d' % -10)
# print ('%+10d' % +10)
# print ('%+10d' % -10)


width = input('Please enter width:')
# width = 35
# print (width)
price_width = 10
# print (price_width)
item_width = int(width) - price_width
# print (item_width)
print ('%-*s' % (item_width,'Item'))
print ('%*s' % (price_width,'Price'))
print ('%-*s%*s' % (item_width,'Item',price_width,'Price'))
print ('-'*int(width))
print ('%-*s%*.2f' % (item_width,'Apple',price_width,0.4))
print ('%-*s%*.2f' % (item_width,'Pears',price_width,0.5))
print ('%-*s%*.2f' % (item_width,'Dried Apricots (16 oz.)',price_width,8))
print ('%-*s%*.2f' % (item_width,'Prunes (4 1bs.)',price_width,12))
print ('='*int(width))
# print ('item',(%width),'price')