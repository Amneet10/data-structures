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




# ...........Count the occurrence of each element from a list...........

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

resultDict = {}
for item in sample_list:
    if item in resultDict:
        resultDict[item] = resultDict[item] + 1
       
    else:
        resultDict[item] = 1
        

# resultDict[11] = count
print(resultDict)


 





    














   
        
