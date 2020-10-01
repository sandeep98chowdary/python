#input int elements to a list
#####################
##a=[]
##n=int(input('enter the no elements:'))
##for i in range(n):
##  a.append(int(input('enter the element :')))
##print(a)  

#initializing a list
#############
##a=[1,'string',1.3,True,33]
##print(a,type(a),sep='\n')


#ACCESSING THE ELEMENTS OF LIST
#################################
##a=['hi','bye',1,2,3.5]
##print(a[0],a[4],a[3])
##print(a[:],a[:5],a[2:],a[1:4],sep='\n')
##print(a[-1],a[0],a[-2])
##print(a[:],a[:-1],a[-3:],a[-4:-1],sep='\n')

#FUNCTIONS ON LIST
###################
##s=[2,1,3,2,4,5,5.1]
##print(len(s))                             #1.lenght
##print(max(s))                           #2.max elem
##print(min(s))                            #3.min elem
##s.sort()                                    #4.sort(asc)   
##print(s)                                   
##s.sort(reverse=True)             #5.sort(dec)
##print(s)                                   
##print(sum(s))                          #6.sum of elem
##print(s.count(3))                     #7.counting repeating of elem
##print(s.index(5))                     #8.index no. of elem

#MANIPULATING LIST
###################
##a=[3,5,8,4,7]
##a.append(55)#9.add an elem at end
##print(a)
##a.append(int(input('enter the element to append:')))
##print(a)
##a.insert(1,'hi')#10.add an elem at given index no.
##print(a)
##a.insert(int(input('enter the index no.:')),int(input('enter the element.:')))
##print(a)
##b=[1,2]
##a.append(b)#11.add a list into a list
##print(a)
##a.extend(b)#12.add the elem of a list into other list
##print(a)
##c=[1,2,3,[4,5]]
##print(c[3][0],c[3][1])#13.accessing an elem of a list inside a list
##d=[1,2,3,'hlo']
##d.reverse()#14.reverse the order
##print(d)

a=[2,4,6,8,3,55,33,44,24]
a.pop()#15.removes the last elem
print(a)
a.pop(1)#16.removes the elem in a index no.
print(a)
del a[3]#17.delets the elem
print(a)
b=[11,12,23,53,45,63,47,624]
del b[:3]
print(b)
del b[3:]
print(b)
c=[1,2,3,4,5,6,7]
del c[1:3]
print(c)
del c[1:-2]
print(c)
c.clear()#clears all elem
print(c)
d=['h','l','o']
del d
print(d)




















