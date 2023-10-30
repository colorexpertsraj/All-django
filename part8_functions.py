# def my_func(param1 = "default"):
#     print("My first Python functions {}".format(param1))
# my_func()


# def my_func(param1 = 'default'):
#
#     """
#     Docstring goes here.
#     """
#
#     print(param1)
# my_func()



# def hello():
#     print("hello")
#
# hello()


# def giveMeHello():
#
#     return "Hello Md Abdur Rajjak"
#
# result = giveMeHello()
# print(result)


# common mistake:

# print(giveMeHello)




# def evenCheck(num):
#     print("I'm checking to see if {} is even ".format(num))
#
#     print(num%2 == 0)
#
# evenCheck(41)





# def helloYou(name = "Md Abdur Rajjak"):
#     return("Hello, "+name)
#
# result = helloYou()
# print(result)



#
# def addNum(num1, num2):
#     return num1+num2
#
# result =  addNum("2", "3")
# print(result)


# def addEvenOnly(num1, num2):
#     """
#     Input: Two numbers
#     OUtput: False if both numbers are not even,
#     the sum if both numbers are even
#
#     """
#
#     if(num1%2!=0) or (num2%2!=0):
#         return False
#     else:
#         return num1+num2
#
#
# x = addEvenOnly(1,2)
# y = addEvenOnly(2,2)
#
# print(x)
# print(y)






# def timesTwo(num):
#     return num*2
# #lambda num: num*2
# value =timesTwo(5)
# print(value)



# my_list = [1,2,3,4,5,6,7,8,9,10]
#
# # def evenBool(num):
# #     return num%2 == 0
# #
# # evens = filter(evenBool, my_list)
# # print(list(evens))
#
#
# evens = filter(lambda num: num%2 ==0, my_list)
# print(list(evens))




# def addNum(num1, num2):
#     if type(num1) == type(num2)== type(10):
#         return num1+num2
#     else:
#         return "Sorry, I need integers"
#
# result = addNum(2, "3")
# print(result)



st = 'Hello my name is Md Abdur Rajjak'
#
# lower = st.lower()
# upper = st.upper()
# split = st.split()
#
# print(lower)
#
# print(upper)
#
# print(split)




tweet = "Go sports #Sports"

print(tweet.split('#'))

# print(tweet.split('#')[1])
