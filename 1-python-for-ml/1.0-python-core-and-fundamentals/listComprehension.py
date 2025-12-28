squares=[x**2 for x in range(6)]
evens=[x for x in range(20) if x%2==0]
temp=[35,40,28,32]
for item in temp:
    print(item,"Degree celcius is ",(item*9/5)+32,"Farenhite")
farenhite=[(item*9/5)+32 for item in temp]
print("darenhite",farenhite)

unique_initials={w[0].lower() for w in ["apple","banana","cherry","avocado","Grape"]}
square_map={x:x**2 for x in range(5)}
print(squares)
print(evens)
print(square_map)
print(unique_initials)

# inner list
innerList=[[x**2 for x in range(i,i+5) if(x%2==0)] for i in range(1,10,3)]
print(innerList)
st={1,2,2,3,"A"}
print(st)
tpl = (1, 2, 3, [4, 5])
tpl[3].append(6)
print(tpl)