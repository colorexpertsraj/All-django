# my_dict = {'key1':'value1', 'key2':'value2'}
#
# print(my_dict['key2'])


my_dict = {'key1':123,'key2':[12,13,14], 'key3':['item0','item1','item3']}

# print(my_dict['key3'])
# print(my_dict['key3'][2])
# print(my_dict['key3'][2].upper())
# print(my_dict['key1'])
# my_dict['key1'] = my_dict['key1'] - 123
#
# print(my_dict)
#
#
my_dict['key1'] -= 123

print(my_dict['key1'])


d = {}

d['animal'] = 'Dog'

d['answer'] = 42


print(d)

print("nested dictionary value:")
d = {'key1':{'nestkey':{'subnestkey':'value'}}}


print(d['key1']['nestkey']['subnestkey'])



print("Create a typical dictionary")


d={'key1':1, 'key2':2, "key3":3}

print(d.keys())



print("method to grab all values")


print(d.values())


print("Method to return tuples of all items:")

print(d.items())
