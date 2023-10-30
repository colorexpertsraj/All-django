def arrayCheck(nums):

    for i in range(len(nums)-2):

        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

arr = arrayCheck([1,1,2,1,2,3])

arr1 = arrayCheck([1,1,2,4,1])

#print(arr)
#print(arr1)

def stringBits(str):
    result = ""


    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result
string = stringBits('Hello')
string1 = stringBits('Heeololeo')
#print(string)
#print(string1)




def end_other(a,b):
    a = a.lower()
    b = b.lower()


    return a[-(len(b)):] == b or a == b[-(len(a)):]

T = end_other('Hijbc', 'abc')

#print(T)




def doubleChar(str):

    result = ''
    for char in str:
        result += char * 2

    return result


d = doubleChar('The')

#print(d)






def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):

    if n in [13, 14, 17, 18, 19]:
        return 0
    return n

no = no_teen_sum(18,2,3)

#print(no)



def count_evens(nums):
    count = 0
    for element in nums:
        if element % 2 == 0:
            count += 1
    return count
counted = count_evens([2,1,2,6,8,3,4])

print(counted)
