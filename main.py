# ..........create a program from given lists for putting odd even numbers and make a new list from that elements.....

# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28,21,27,31]
# l3 = []
# for i in l1:
#     if (i  % 2 ) != 0:
#         l3.append(i)
# for i in l2:
#     if(i % 2)== 0:
#         l3.append(i)

# print(l3)



# .........Create a list by picking an odd-index items from the first list and even index items from the second......

# ......Slice list into 3 equal chunks and reverse each chunk.....


# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# print(f'original list:{sample_list}')

# length =len(sample_list)
# firstPart =int(length/3)
# start = 0
# end = firstPart



 




# # # .....Python program to interchange first and last elements in a list......
    



# # sampleString = "My name is Amneet. I live in Canada. I done my Master's in Computer Science . Canada is a beautiful City"
# # resultDict = {}

# # for item in sampleString.split():
# #     if item in resultDict:
# #         resultDict[item] = resultDict[item] + 1

# #     else:
# #         resultDict[item] = 1
# # print(resultDict)



# def Calander(Months):
  
#     if Months == 'August':
#         print(f'Cool,Its My Birthday Month {Months}')

#     elif Months == 'June':
#         print(f'Yeah,Its My Husband Bithday Month {Months}')
#     else:
#         print('Oops')

# Calander('August')


# ........Multiple Parameters......

# def AddTwoNumbers(a,b):
#     sum = a + b
#     return sum


# print(AddTwoNumbers(3,4))


# .........Infinite Loop.......

# friends = ['Gagan','Kuldeep','Jonu']
# for i in friends:
#     print(f'Happy Birthday :{i}' )
# # print('Done!')


# largestNumber_so_far = -1
# print('before',largestNumber_so_far)
# for i in [2,45,67,12,46,67,89,2]:
#     if i > largestNumber_so_far:
#         largestNumber_so_far = i
#     print(largestNumber_so_far,i)
# print('after',largestNumber_so_far)



# smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         # break
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)



#............... Create Dictionary................

from unicodedata import name


person = {"Name" :'Amneet',"Country":"Canada","Status":"PR"}


# .........Dictionary Created as a Pair........
person = dict([("Name","Amneet"),("Country","Canada"),("Status","PR")])

# .............Dictionary As a Pair using List 
listOFElement = [[12,3],[4,6],[6,7]]
newDict = dict(listOFElement)


person = {"Name":"Amneet","Country":["India","Canada"]}



# .........Create an Dictionary as a Mixed keys...........

person = {"Name":"Amneet","Mobile" :122356466}


# ............Empty Dictionary..........

person = {}


# ......Retrieve values from Dictionary..........

person = {"Name" :'Amneet',"Country":"Canada","Status":"PR"}


# ......Second Method.........
person= {"Name" :'Amneet',"Country":"Canada","Status":"PR"}


for key,value in person.items():
    print(key,value)


# ....Best method to retrieve the value is using Get method because its error safe...its hand program gracefully....



#.... One way to add something in dict....



# ....second method using update method ......

# deleted last item from the dict that last inserted.....
person = {"Name" :"Amneet","Country":"Canada","Status":"PR"}


del person["Country"]
print(person)
person.clear()
print(person)

