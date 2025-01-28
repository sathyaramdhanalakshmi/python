L1=[] #
print(" 1.empty list ",L1)

L2=[1,2,3,4,5]
print("\n 2.list with five elements ",L2)

L3=['hii',['hello','dhana']]
print("\n 3.nested List ",L3)

L4=list('spam')
print("\n 4.list created from string spam ",L4)

L5=list(range(-3,4))
print("\n 5.list with items in the range from -3 to 3 ",L5)

L6=[10, 20, 30, 40, 50]
print("\n 6.element at index 2 is ",L6[2])

L7=['a',[12,23,34],'c']
print("\n 7.nested list with different data types ",L7[1][2])

L8=[1,2,3,4,5,6,7,8]
print("\n 8.slicing the given list into another ",L8[2:5])
print("\n 9.length of list",len(L8))

L9=[10,20,30,40,50]
sum=0
length=len(L9)
for i in range(length):
    sum+=L9[i]
print("\n the sum element of list ",L9,"is: ",sum)

res=[c*4 for c in 'SPAM']
print(res)