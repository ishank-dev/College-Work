#i)
l1=[]
for i in range(5):
        l1.append(int(input()))

#ii)
print("Max element: ",max(l1),"\nMin element: ",min(l1))

#iii)
l1.append(7)

#iv)
l1.remove(7)

#v)
print("Enter element to be searched: ")
if int(input()) in l1:
    print("Element found")
else:
    print("Element not found")

#Use .index() for location, returns location, or ValueError if not exists