#Create two lists. The first list should consist of odd numbers. The second list is also of even numbers.

oddList = [1,3,5,7,9,]
evenList = [2,4,6,8,10]

#Merge two lists. Multiple all values in the new list by 2.

mergedList = evenList + oddList

multpList=[]
for x in (mergedList):
    multpList.append(x*2)



print(f"Tek sayıları içeren liste: {oddList}")
print(f"Çift sayıarı içeren liste: {evenList}")
print(f"Birleştirilmiş ve indexleri 2 ile çarplılmış yeni liste: {multpList}")
print("Yeni listenin indexlerinin veri tipleri; ")


#Use a loop to print data type of the all values in the new list.
for index in multpList:
    print(type(index))



