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


sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print(f'original list:{sample_list}')

length =len(sample_list)
firstPart =int(length/3)
start = 0
end = firstPart



for i in range(3):
   indexes = slice(start,end)


   listchunck =sample_list[indexes]
   print(i,listchunck)

















   
        
