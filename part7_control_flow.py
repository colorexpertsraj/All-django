# # Greater than
#
#
# 1>2
#
# # Less than
#
# 1<2
#
# #Greater than or Equal # TODO:
# 1>=1
#
# # Less than equal to
#
# 1<=4
#
# # Eqality
#
# 1 == 1
#
# 1 == "1"
#
# 'hi' == 'bye'
#
# print(1 == 1)
#
#
# print('hi' == 'bye')
#
# print(1 != 1)
# print(1 != "1")


# LOGICAL OPERATOR

# #AND
# print((1>2) and (2<3))
#
# #OR
# print((1>2) or (2<3))
#
# # MULTIPLE OPERATOR LOGICAL
#
#
# print((1 == 2 ) or (2 == 3) or (4 == 4))


# if 1<2:
#
#     print('yes!')
#
# if 3<2:
#
#     print('yes!')
#
# else:
#     print('No')



#
#
# if 1<2:
#     if 2<3:
#         print('true')



# if 1<2:
#     print('First Block')
#     if 20>3:
#         print('Second block')




# if 1>2:
#     print("hello")
# elif 3 == 3:
#     print('elif ran')
# else:
#     print('last')

#
#
# if 1 == 1:
#     if 1>2:
#         print("hello")
#     elif 3 == 3:
#         print('elif ran')
#     else:
#         print('last')




# LOOPS FOR LOOPS:


# seq = [1,2,3,4,5,6]
#
# for item in seq:
#
#     # code here
#     print(item)

#LIST

# seq = [1,2,3,4,5,6]
#
# for item in seq:
#
#     # code here
#     print(item)




# DICTIONARY



# d = {"raj":1, "color":2, "Clipping":3}
#
#
# for item in d:
#     print(item)





# d = {"raj":1, "color":2, "Clipping":3}
#
#
# for k in d:
#     print(k)
#     print(d[k])



# mypairs = [(1,2),(3,4),(5,6)]
#
# for item in mypairs:
#     print(item)


# tuples unpacking:
#
# mypairs = [(1,2),(3,4),(5,6)]
#
# for (tup1, tup2) in mypairs:
#     print(tup1)
#     print(tup2)


#
# mypairs = [(1,2),(3,4),(5,6)]
#
# for tup1, tup2 in mypairs:
#     print(tup1)
#     print(tup2)




#WHILE LOOPS:


# i = 1
# y = 10
#
# while i<5:
#     print("i is: {} and y is {}".format(i, y))
#     i = i+1
#     y = y+1






# r = [9,5,38,4,8,6]
#
# print(range(5))
#
# print(list(range(0, 5)))
#
# print(list(range(0, 20, 2)))
#
# print(r)


#
# for item in range(10):
#
#     print(item)


#
# x = [1,2,3,4]
#
# out = []
#
# for num in x:
#     out.append(num**2)
#
# print(out)






x = [1,2,3,4]

out = [num**2 for num in x]

print(out)
