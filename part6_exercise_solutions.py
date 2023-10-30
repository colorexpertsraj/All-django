s = 'django'

print(s[0])
print(s[-1])

print(s[:4])


print(s[1:4])

print(s[4:])


print(s[::-1])



###############
## Problem 2 ##
###############


l = [3,7,[5,1,'hello']]

# print(l[2][2])

l[2][2] = "goodbye"


print(l)


###############
## Problem 3 ##
###############

d1 = {'simple_key' : 'hello'}

print(d1['simple_key'])


d2 = {'k1':{'k2':'Abdur Rajjak'}}

print(d2['k1']['k2'])





d3 = {'k1':[{'nest_key':['this is deep', ['Hello Raj']]}]}

print(d3['k1'][0]['nest_key'][1][0])




###############
## Problem 4 ##
###############



mylist=[1,5,4,6,4,5,4,65,5,5,54]

print(set(mylist))



###############
## Problem 5 ##
###############



age = 24

name = "Md Abdur Rajjak"


print("Hello my name is {} and my old is {} years old".format(name, age))
